from ctypes import ArgumentError
from manimlib import *

class classproperty(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)

class Bpm:
    DEFAULT_BPM: float = 180

    bpm: float = DEFAULT_BPM

    @classproperty
    def seconds_per_beat(self) -> float:
        return 60 / self.bpm



class Lyric(Text, Bpm):
    _scale = 1
    _opacity = 1
    _color = WHITE

    def __init__(self, words:list[str | list[str]], word_break_pos=1,  **kwargs):
        self.kwargs = kwargs
        flattened_words = [word 
                           if isinstance(word, str) 
                           else ''.join(word) 
                           for word in words]
        if word_break_pos == 1:
            super().__init__(' '.join(flattened_words) + ' -', **kwargs)
            self.word_break = self[-1].set_opacity(0)
            self.prefix = '^'
            self.postfix = self.text[:-1] + r'(?=-$)'
        elif word_break_pos == -1:
            super().__init__('-' + ' '.join(flattened_words) + ' ', **kwargs)
            self.word_break = self[0].set_opacity(0)
            self.prefix = '(?<=^-)'
            self.postfix = self.text[1:]
        else:
            super().__init__(' '.join(flattened_words) + ' ', **kwargs)
            self.prefix = '^'
            self.postfix = self.text[1:]

        self.prefix_string = ''
        self.words = words
        self.set_opacity(0, True)
        self.scale(self._scale)
        self.set_color(self._color)

    def colour_part(self, part: str, color: str, index=0):
        self.select_part(part, index=index).set_color(color)

    def generate_word_animation(self, word: str, timing: float, add_space=True) -> Animation:
        actual_word = f'{word} ' if add_space else word
        # actual_timing = timing * self.seconds_per_beat
        self.prefix_string += actual_word
        self.postfix = self.postfix[len(actual_word):]
        part = VGroup(self.select_part(re.compile(self.prefix + re.escape(self.prefix_string))))
        return ApplyMethod(part.set_opacity, self._opacity, True, rate_func=np.ceil, run_time=timing)

    @staticmethod
    def fix_timing(timings):
        if timings == []:
            return []
        if isinstance(timings[0], (float, int)):
            part = timings[0] * Lyric.seconds_per_beat
        else:
            part = Lyric.fix_timing(timings[0])
        return [part] + Lyric.fix_timing(timings[1:])

    def play_to_bpm(self, timings):
        if len(timings) != len(self.words):
            raise ArgumentError(f'these lengths must be the same:\n\t{len(timings)=}\n\t{len(self.words)=}\n\t{timings=}\n\t{self.words=}')

        timings = self.fix_timing(timings)
        animation_parts = []
        for word, timing in zip(self.words, timings):
            if isinstance(word, str):
                animation_parts.append(self.generate_word_animation(word, timing))
            else:
                for (word_part, timing_part) in zip(word[:-1], timing[:-1]):
                    animation_part = self.generate_word_animation(word_part, timing_part, add_space=False)
                    def gen_change(postfix):
                        def change(word_break):
                            word_break.align_to(self.select_part(re.compile(postfix)), LEFT)
                            word_break.set_opacity(self._opacity)
                            return word_break
                        return change
                    word_break_animation = ApplyFunction(gen_change(self.postfix), self.word_break, rate_func=np.ceil, run_time=timing_part)
                    animation_parts.append(AnimationGroup(animation_part, word_break_animation))
                animation_part = self.generate_word_animation(word[-1], timing[-1])
                word_break_animation_opacity = ApplyMethod(
                        self.word_break.set_opacity, 
                        0,
                        rate_func=np.ceil,
                        run_time=timing[-1])
                animation_parts.append(AnimationGroup(animation_part, word_break_animation_opacity))
        return Succession(*animation_parts)

class Lyrics(VGroup): 
    def __init__(self, lyrics, word_break_pos = 1, aligned_edge=ORIGIN, **kwargs):
        self.word_break_pos = word_break_pos
        self.kwargs = kwargs
        super().__init__(*list(map(self.configure_lyric, lyrics)))
        self.arrange(DOWN, aligned_edge=aligned_edge)

    def configure_lyric(self, lyric):
        if isinstance(lyric, tuple):
            return Lyric(lyric[0], self.word_break_pos, **self.kwargs).scale(lyric[1]['scale']) # can be generalised
        return Lyric(lyric, self.word_break_pos, **self.kwargs)

    def play_to_bpm(self, timingses):
        if len(timingses) != len(self.submobjects):
            raise ArgumentError(f'these lengths must be the same:\n\t{len(timingses)=}\n\t{len(self.submobjects)=}')

        return Succession(*[submobject.play_to_bpm(timings) for (submobject, timings) in zip(self.submobjects, timingses)])


def scale(lyric: list[str], scale=1):
    return (lyric, {'scale': scale})

def split(lyric_str: str):
    return lyric_str.split(' ')

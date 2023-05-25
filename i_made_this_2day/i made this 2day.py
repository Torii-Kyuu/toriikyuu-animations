import sys
import os
sys.path.append(os.getcwd())

from lyricslib import *

class Debug(Scene):
    def construct(self):
        self.embed()


class IMadeThis2Day(Scene):
    def construct(self):
        self.camera.background_rgba = [0, 0, 0, 1]
        self.add_sound('I_made_myself_do_it_v2.mp3')


        Lyric.bpm = 160
        Lyric._scale = 1.2
        Lyric._color = '#00FFFF'

        lyrics = Lyrics([
                ['if you want to try being in the style'],
                ['then listen up on faves'],
                ['learn the core vocabulary'],
                ['rhymes and don\'t forget the bass'],
            ], word_break_pos=0)
        lyrics[0].colour_part('style', '#FFC0CB')
        lyrics[3].colour_part('bass', '#FF0000')
        lyrics.arrange(DOWN, aligned_edge=LEFT, buff=1.5, center=False)
        lyrics.to_edge(UL)

        Lyric._scale = 2

        tokiponalyric = Lyric((['\nkijetesantakalu '] + ['kijetesantakalu ']*7)*4, word_break_pos=0, font='Fairfax Pona HD', disable_ligatures=False)
        tokiponalyric.set_color_by_gradient(BLUE, GREEN, ORANGE)
        tokiponalyric.set_opacity(1)
        # self.add(tokiponalyrics)
        # self.play(tokiponalyrics.play_to_bpm([[1]*8]*4))
        self.play(ShowIncreasingSubsets(tokiponalyric, run_time = 32 * Lyric.seconds_per_beat))
        self.remove(tokiponalyric)
        
        Lyric._scale = 1.2
        
        # self.wait(32 * Lyric.seconds_per_beat)
        self.add(lyrics)
        self.play(lyrics.play_to_bpm([[4.7], [3.3], [4], [4]]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['I don\'t think a day is a'],
                ['remarkably large time space'],
                ['I\'ll cut myself short here'],
                ['now on to sophisticated case'],
            ], word_break_pos=0)
        lyrics[1].colour_part('time space', '#8b2377')
        lyrics.arrange(DOWN, aligned_edge=RIGHT, buff=1.5, center=False)
        lyrics.to_edge(UR)

        self.add(lyrics)
        self.play(lyrics.play_to_bpm([[4], [4], [3.7], [4.3]]))
        self.remove(lyrics)

        square1 = Square().scale(3).set_color(BLUE)
        square2 = Square().scale(3).set_color(ORANGE)
        circle = Circle().scale(3).set_color(GREEN)
        self.add(square1)
        self.play(Transform(square1, circle), run_time = 12 * Lyric.seconds_per_beat)
        # self.wait(12 * Lyric.seconds_per_beat)
        Lyric.bpm = 180
        self.play(Transform(square1, square2), run_time = 3 * Lyric.seconds_per_beat)
        self.remove(circle, square1, square2)
        # self.wait(3 * Lyric.seconds_per_beat)

        Lyric._scale = 1.7

        lyrics = Lyrics([
                ['through', 'the', 'haze'],
                ['of', 'simple', 'dreams']
            ])
        lyrics[1].colour_part('dreams', ORANGE)

        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [1/2, 1/2, 1],
                [0.8, 1.4, .8]
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['genre'],
                [['conglo', 'merate']],
                [['ap', 'pears']],
            ])
        lyrics[2].colour_part('appears', ORANGE)


        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [1],
                [[1,1]],
                [[1/2, 1/2]],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['is', 'that'],
                ['how', 'it', 'feels?'],
            ])
        lyrics[1].colour_part('feels', ORANGE)


        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [1, .8],
                [.6, .6, 1],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['to', 'be', ['cre', 'a', 'tor'], 'of', 'what\'s'],
                scale(['RIL'], 3),
            ])
        lyrics[1].colour_part('RIL', ORANGE)


        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [.5, .5, [.5, .5, .5], .5, .7],
                [.3],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['a', ['la', 'yer'], ['be', 'ing']],
                ['pilled', 'off'],
            ])
        lyrics[0].colour_part('being', ORANGE)
        lyrics[1].colour_part('pilled', ORANGE)


        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [.5, [1, .8], [.6, .6]],
                [.5, 1],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['of', 'a', 'tree'],
                ['that', 'will', ['re', 'veal']],
            ])
        lyrics[0].colour_part('tree', ORANGE)
        lyrics[1].colour_part('will reveal', ORANGE)



        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [.5, .5, 1],
                [.5, .5, [.5, .5]],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['what', 'I', 'am', ['a', 'fter']],
            ])

        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [1, .5, 1, [1, 1]],
            ]))
        self.remove(lyrics)

        lyrics = Lyrics([
                ['and', 'where', 'does', 'it', 'lead'],
            ])
        lyrics[0].colour_part('lead', ORANGE)


        self.add(lyrics)
        self.play(lyrics.play_to_bpm([
                [.5, 1, .5, .5, 1],
            ]))
        self.remove(lyrics)
        self.wait(1)

        credits = Lyric(['I made this in 2days\nmusic, lyrics, video: Torii Kyuu'], word_break_pos=0)
        credits.set_color(BLUE)
        credits.colour_part('2', GREEN)
        credits.colour_part('days', ORANGE)
        credits.colour_part('Torii Kyuu', '#00ffb7')
        [credits.colour_part(x, '#CB73C7') for x in ['music', 'lyrics', 'video']]
        credits.scale(0.6)
        credits.set_opacity(1)
        self.add(credits)
        self.wait(4)



        # self.remove(lyrics)
        # lyric1 = Lyric(split('if you')).to_edge(UL)
        # lyric2 = Lyric(split('want to')).to_edge(UR)
        # lyric3 = Lyric(split('try')).next_to(lyric1, DOWN)
        # lyric4 = Lyric(split('being in the')).next_to(lyric2, DOWN)
        # lyric5 = Lyric(split('style')).set_color(LIGHT_PINK)
        # self.play(lyric1.play_to_bpm([1/3, 2/3]))
        # self.play(lyric2.play_to_bpm([1/3, 2/3]))
        # self.play(lyric3.play_to_bpm([3/4]))
        # self.play(lyric4.play_to_bpm([5/4/3]*3))
        # self.play(lyric5.play_to_bpm(h))


        # lyrics = Lyrics([
        #         ['if', 'you', 'want', 'to'],
        #         ['try'],
        #         ['being', 'in', 'the'], 
        #         ['style']
        #     ])
        # lyrics.arrange(DOWN, aligned_edge=ORIGIN, buff=0.7)
        # # lyrics.to_edge(UL)
        # lyrics.set_color(BLUE)
        # lyrics[-1].select_part("style").set_color(LIGHT_PINK)
        # self.play(lyrics.play_to_bpm([
        #         h*4, h, h*3, h
        #     ]))
        self.embed()

        # lyrics = Lyrics([
        #         split("If you want to try being in the style"),
        #         split("than listen up on faves"),
        #         split("learn the core vocabulary"),
        #         split("rhymes and don't forget the bass"),
        #     ])

        # lyrics.arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        # lyrics.to_edge(UL)
        # lyrics.set_color(BLUE)
        # self.wait(2)
        # self.play(lyrics.play_to_bpm([
        #         [1/3, 2/3]*4 + [1/2],
        #         [h, 1, h, h, w],
        #         [1]*4,
        #         [4/6]*6
        #     ]))


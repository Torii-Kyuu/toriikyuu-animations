from manimlib import *

import sys
import os
sys.path.append(os.getcwd())

from finda import *

class ForFreya(Scene):
    def construct(self):
        self.camera.frame.scale(.2).move_to(RIGHT*0.5 + UP*0.3)
        self.camera.background_rgba = [0.05, 0.1, 0.15, 1]

        clothoid_line = Line(3*LEFT, ORIGIN).set_color("#ffffff")
        clothoid_line_dark = Line(ORIGIN, 3*RIGHT).set_color("#39424b")

        # 715 is 1

        L = ValueTracker(.2)
        theta = ValueTracker((90 - 12)/360*PI)
        delta_x = ValueTracker(1)

        a = ValueTracker(0) \
        .add_updater(lambda a: 
            a.set_value(solve(L.get_value(), theta.get_value(), delta_x.get_value())))
        x = ValueTracker(0) \
        .add_updater(lambda x: 
            x.set_value(get_fxy(L.get_value(), theta.get_value(), delta_x.get_value()).x(a.get_value())))
        y = ValueTracker(0) \
        .add_updater(lambda y: 
            y.set_value(get_fxy(L.get_value(), theta.get_value(), delta_x.get_value()).y(a.get_value())))
        
        x_line = Line(ORIGIN, ORIGIN) \
            .add_updater(lambda x_line:
                x_line.set_points_by_ends(UP*y.get_value(), UP*y.get_value() + RIGHT*x.get_value())) \
            .set_color("#db3e1d")

        y_line = Line(ORIGIN, ORIGIN) \
            .add_updater(lambda y_line:
                y_line.set_points_by_ends(RIGHT*x.get_value(), RIGHT*x.get_value() + UP*y.get_value())) \
            .set_color("#9af348")

        


        pn_1 = Dot(ORIGIN).scale(.2)
        pn = Dot(ORIGIN).add_updater(lambda pn: pn.move_to(RIGHT * delta_x.get_value())).scale(.2)

        up_clothoid_line_dark = Line(ORIGIN, ORIGIN) \
        .add_updater(lambda up_clothoid_line_dark:
           up_clothoid_line_dark.set_points_by_ends(pn.get_center(), 
            pn.get_center() + 3*np.array([-cos(2 * theta.get_value()), sin(2 * theta.get_value()), 0]))).set_color("#39424b")

        curve = ParametricCurve(lambda t: (C(t), S(t), 0), (0, L.get_value(), .05)).set_color("#32b4f6")
        curve.add_updater(lambda curve: curve.become(ParametricCurve(lambda t: (C(t)*a.get_value(), S(t)*a.get_value(), 0), (0, L.get_value()/a.get_value(), .05)).set_color("#32b4f6")))

        curve_end = ValueTracker(np.array([0, 0, 0])) \
            .add_updater(lambda curve_end:
                curve_end.set_value(np.array([C(L.get_value()/a.get_value())*a.get_value(), S(L.get_value()/a.get_value())*a.get_value(), 0])))

        perp = Line(ORIGIN, ORIGIN) \
            .add_updater(lambda perp:
                perp.set_points_by_ends([x.get_value(), y.get_value(), 0], curve_end.get_value())) \
            .set_color("#e52d63")

        radius = ValueTracker(0) \
            .add_updater(lambda radius: 
                radius.set_value(np.linalg.norm(np.array([x.get_value(), y.get_value(), 0]) - curve_end.get_value())))
        circle = Circle().add_updater(
            lambda circle:
                circle.become(Circle(arc_center = (x.get_value(), y.get_value(), 0), radius = radius.get_value())).set_color("#226f98"))

        text_x = Text("x").set_color("#db3e1d").scale(.15).add_updater(lambda text_x: text_x.next_to(x_line, UP, aligned_edge=DOWN, buff=0.03))
        text_y = Text("y").set_color("#9af348").scale(.15).add_updater(lambda text_y: text_y.next_to(y_line, LEFT, aligned_edge=RIGHT, buff=0.03))
        text_L = Text("L").set_color("#32b4f6").scale(.15).add_updater(lambda text_L: text_L.next_to(curve, UP, buff=-0.1))
        text_pn_1 = Tex("P_{n-1}").scale(.15).add_updater(lambda text_pn_1: text_pn_1.next_to(pn_1, DOWN, aligned_edge=UP, buff=0.03))
        text_pn = Tex("P_n").scale(.15).add_updater(lambda text_pn: text_pn.next_to(pn, RIGHT + DOWN, buff=0.03))

        text_a = Text(f"a = {a.get_value()}")
        text_a.add_updater(lambda text_a: text_a.become(Text(f"a = {round(a.get_value(), 3)}\nL = {round(L.get_value(), 3)}\ntheta = {round(theta.get_value(), 2)}\ndelta_x = {round(delta_x.get_value(), 2)}").scale(.15).move_to(0.2*(DOWN + LEFT))))

        self.add(clothoid_line,
                 clothoid_line_dark,
                 up_clothoid_line_dark,
                 x_line,
                 y_line,
                 curve,
                 circle,
                 perp,
                 pn_1,
                 pn,
                 text_x, text_y, text_L, text_pn_1, text_pn, text_a,
                 L, theta, delta_x, a, x, y, curve_end, radius)

        self.play(L.animate.set_value(0.7), run_time=3, rate_func=linear)
        self.play(theta.animate.set_value(PI/8), L.animate.set_value(0.3), run_time=4, rate_func=linear)
        self.play(theta.animate.set_value(PI/3), delta_x.animate.set_value(0.6), run_time=4, rate_func=linear)
        self.play(L.animate.set_value(1), delta_x.animate.set_value(1), run_time=4, rate_func=linear)
        # log stuff

        # print(f'\n{a.get_value()=}')
        # print(f'\n{L.get_value()=}')
        # print(f'\n{theta.get_value()=}')
        # print(f'\n{delta_x.get_value()=}')
        # print(f'\n{solve(L.get_value(), theta.get_value(), delta_x.get_value())=}\n')
        # print(f'\n{x.get_value()=}')
        # print(f'\n{y.get_value()=}')


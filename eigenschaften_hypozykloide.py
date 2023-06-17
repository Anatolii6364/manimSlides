from manim import *
from manim_slides import Slide

def epicycloid_func(R, r, c, t):
    return np.array([
        (R + r)*np.cos(t) + c*np.cos((-(R + r)/r)*t),
        (R + r)*np.sin(t) - c*np.sin((-(R + r)/r)*t),
        0
    ])


def hypocycloid_func(R, r, c, t):
    return np.array([
        (R - r)*np.cos(t) + c*np.cos(((R - r)/r)*t),
        (R - r)*np.sin(t) - c*np.sin(((R - r)/r)*t),
        0
    ])


def epicycloid(n, d, k, s=1):
    R = 1
    r = d/n

    if c == None:
        c = r

    big = Circle(R, color=WHITE).scale(s)
    curve = always_redraw(lambda: ParametricFunction(lambda t:
                                                     epicycloid_func(
                                                         R, r, c, t)*s,
                                                     color=RED, t_range=np.array([0.001, k.get_value()*d])).shift(big.get_center()))

    small = always_redraw(lambda: Circle(r, color=WHITE).scale(s).shift(
        big.get_center() + np.array([(R+r)*s*np.cos(k.get_value()*d), (R+r)*s*np.sin(k.get_value()*d), 0])))

    small_center = always_redraw(lambda: Dot(small.get_center()).scale(s))

    dot = always_redraw(
        lambda: Dot(epicycloid_func(R, r, c, k.get_value()*d)*s).shift(big.get_center().scale(s)))

    radius_line = always_redraw(lambda: Line(
        small.get_center(), dot.get_center(), color=YELLOW))

    txt = MathTex("R = \\frac{" + str(n) + "}{" + str(d) + "}, r = 1", font_size=30).scale(s).next_to(big, DOWN)
    return VDict({'curve': curve,
                  'radius_line': radius_line,
                  'big': big,
                  'small': small,
                  'dot': dot,
                  'small_center': small_center,
                  'label': txt})


def hypocycloid(n, d, k, s=1, c=None):
    R = 1
    r = d/n

    if c == None:
        c = r

    big = Circle(R, color=WHITE).scale(s)
    curve = always_redraw(lambda: ParametricFunction(lambda t:
                                                     hypocycloid_func(
                                                         R, r, c, t)*s,
                                                     color=RED, t_range=np.array([0.001, k.get_value()*d])).shift(big.get_center()))

    small = always_redraw(lambda: Circle(r, color=WHITE).scale(s).shift(
        big.get_center() + np.array([(R-r)*s*np.cos(k.get_value()*d), (R-r)*s*np.sin(k.get_value()*d), 0])))

    small_center = always_redraw(lambda: Dot(small.get_center()).scale(s))

    dot = always_redraw(
        lambda: Dot(hypocycloid_func(R, r, c, k.get_value()*d)*s).shift(big.get_center()).scale(s))

    radius_line = always_redraw(lambda: Line(
        small.get_center(), dot.get_center(), color=YELLOW))

    txt = MathTex("R = \\frac{" + str(n) + "}{" + str(d) + "}, r = 1", font_size=30).scale(s).next_to(big, DOWN)
    return VDict({'curve': curve,
                  'radius_line': radius_line,
                  'big': big,
                  'small': small,
                  'dot': dot,
                  'small_center': small_center,
                  'label': txt})


class BasicExample(Slide):
    def construct(self):

        headline = MathTex("R = \\frac{n}{d}, r = 1").to_edge(UP).to_edge(RIGHT)

        txt1 = MathTex("n > d").to_edge(UP).to_edge(LEFT)
        txt2 = MathTex("ggT(n, d) = 1").next_to(txt1, DOWN).to_edge(LEFT)

        k = ValueTracker(0.001)
        scale = 0.7
        hc1 = hypocycloid(2, 1, k, scale)
        hc2 = hypocycloid(3, 1, k, scale)
        hc3 = hypocycloid(5, 1, k, scale)
        hc4 = hypocycloid(3, 2, k, scale)
        hc5 = hypocycloid(5, 2, k, scale)
        hc6 = hypocycloid(7, 2, k, scale)
        hc7 = hypocycloid(4, 3, k, scale)
        hc8 = hypocycloid(5, 3, k, scale)
        hc9 = hypocycloid(7, 3, k, scale)

        hcGroup1 = VGroup(hc1, hc2, hc3, hc4, hc5, hc6, hc7, hc8, hc9).arrange_in_grid()

        self.play(FadeIn(hcGroup1, headline, txt1, txt2))

        self.wait()

        to_angle = 2*np.pi
        self.play(k.animate.set_value(to_angle),
                  rate_function=smooth,
                  run_time=6
                  )

        self.wait()
        hcGroup1.remove(hc5)
        hcGroup1.remove(hc8)

        k = ValueTracker(0.001)

        hcA = hypocycloid(5, 3, k, 1.5)
        hcB = hypocycloid(5, 2, k, 1.5)
        hcGroup2 = VGroup(hcA, hcB).arrange_in_grid()
        self.play(
            FadeOut(hcGroup1),
            ReplacementTransform(VGroup(hc5, hc8), hcGroup2))

        self.wait()
        self.remove(hcGroup1)

        self.play(k.animate.set_value(to_angle),
                  rate_function=smooth,
                  run_time=12
                  )

        k = ValueTracker(0.001)

        hcC = hypocycloid(8, 1, k, 1.5)
        hcD = hypocycloid(8, 7, k, 1.5)
        hcGroup3 = VGroup(hcC, hcD).arrange_in_grid()

        self.play(
            ReplacementTransform(hcGroup2, hcGroup3))

        self.wait()

        self.play(k.animate.set_value(to_angle),
                  rate_function=smooth,
                  run_time=12
                  )
from manim import *
from manim_slides import Slide


def epicycloid_func(R, r, c, t):
    return np.array([
        (R + r)*np.cos(t) - c*np.cos(((R + r)/r)*t),
        (R + r)*np.sin(t) - c*np.sin(((R + r)/r)*t),
        0
    ])


def epicycloid(n, d, k, s=1, c=None):
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
        big.get_center() + np.array([(R+r)*np.cos(k.get_value()*d), (R+r)*np.sin(k.get_value()*d), 0])*s))

    small_center = always_redraw(lambda: Dot(small.get_center()).scale(s))

    dot = always_redraw(
        lambda: Dot(epicycloid_func(R, r, c, k.get_value()*d)*s).shift(big.get_center()).scale(s))

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

        to_angle = 2*np.pi
        k = ValueTracker(to_angle)
        scale = 0.7
        hc1 = epicycloid(5, 1, k, scale)
        hc2 = epicycloid(5, 2, k, scale)
        hc3 = epicycloid(5, 3, k, scale)

        hcGroup1 = VGroup(hc1, hc2, hc3).arrange()


        self.play(FadeIn(hcGroup1, headline, txt1, txt2))

        self.wait()

        self.play(k.animate.set_value(to_angle*2),
                  rate_function=smooth,
                  run_time=6
                  )
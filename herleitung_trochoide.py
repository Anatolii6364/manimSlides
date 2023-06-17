from manim import *
from manim_slides import Slide

def hypocycloid_func(R, r, c, t):
    return np.array([
                (R - r)*np.cos(t) + c*np.cos(((R - r)/r)*t),
                (R - r)*np.sin(t) - c*np.sin(((R - r)/r)*t), 
                0
            ])

def hypocycloid(R, r, c, k):
    big = Circle(R, color=WHITE)
    curve = always_redraw(lambda: ParametricFunction(lambda t: 
            hypocycloid_func(R, r, c, t),
            color=RED, t_range = np.array([0.001, k.get_value()])).shift(big.get_center()))

    small = Circle(r, color=WHITE)
    small.shift((R-r)*RIGHT)
    small_center = Dot(small.get_center())
    dot = always_redraw(
        lambda: Dot(hypocycloid_func(R, r, c, k.get_value())).shift(big.get_center()))

    radius_line = always_redraw(lambda: Line(small.get_center(), dot.get_center(), color=RED))
    return VDict({'radius_line': radius_line,
                  'curve': curve,
                  'big': big, 
                  'small': small,
                  'dot': dot,
                  'small_center': small_center})

class BasicExample(Slide):
    def construct(self):
        HC = Text("Hypotrochoide").to_edge(UP)
        hX1=MathTex("x(t)= (", "R-r", ")\\cdot\\cos(t)", "+", "r", "\\cdot\\cos\\left(", "\\frac{R-r}{r}\\cdot t", "\\right)",font_size=35).next_to(HC, DOWN)
        hY1=MathTex("y(t)= (", "R-r", ")\\cdot\\sin(t)", "-", "r", "\\cdot\\sin\\left(", "\\frac{R-r}{r}\\cdot t", "\\right)", font_size=35).next_to(hX1, DOWN)

        EC = Text("Epitrochoide").next_to(hY1, DOWN)
        eX1=MathTex("x(t)= (", "R+r", ")\\cdot\\cos(t)", "-", "r", "\\cdot\\cos\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)",font_size=35).next_to(EC, DOWN)
        eY1=MathTex("y(t)= (", "R+r", ")\\cdot\\sin(t)", "-", "r", "\\cdot\\sin\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)", font_size=35).next_to(eX1, DOWN)


        k = ValueTracker(0.001)
        hcg1 = hypocycloid(2.5, 1, 1, k).shift(LEFT*3.5)

        rText = Text("r", font_size=30).next_to(hcg1['radius_line'], UP).set_color(RED)

        self.play(FadeIn(EC, HC))

        self.wait()

        self.play(FadeIn(hX1, hY1, eX1, eY1))
        self.play(Group(HC, hX1, hY1, EC, eX1, eY1).animate.shift(RIGHT*3), FadeIn(hcg1))


        # ...
        hX2=MathTex("x(t)= (", "R-r", ")\\cdot\\cos(t)", "+", "c", "\\cdot\\cos\\left(", "\\frac{R-r}{r}\\cdot t", "\\right)",font_size=35).next_to(HC, DOWN)
        hX2[4].set_color(RED)
        hY2=MathTex("y(t)= (", "R-r", ")\\cdot\\sin(t)", "-", "c", "\\cdot\\sin\\left(", "\\frac{R-r}{r}\\cdot t", "\\right)", font_size=35).next_to(hX2, DOWN)
        hY2[4].set_color(RED)

        eX2=MathTex("x(t)= (", "R+r", ")\\cdot\\cos(t)", "-", "c", "\\cdot\\cos\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)",font_size=35).next_to(EC, DOWN)
        eX2[4].set_color(RED)
        eY2=MathTex("y(t)= (", "R+r", ")\\cdot\\sin(t)", "-", "c", "\\cdot\\sin\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)", font_size=35).next_to(eX2, DOWN)
        eY2[4].set_color(RED)

        # ...

        self.wait()

        self.play(hX1[4].animate.set_color(RED), hY1[4].animate.set_color(RED),
                  eX1[4].animate.set_color(RED), eY1[4].animate.set_color(RED),
                  FadeIn(rText))

        self.wait()

        hcg2 = hypocycloid(2.5, 1, 1.5, k).shift(LEFT*3.5)
        hcg3 = hypocycloid(2.5, 1, 0.5, k).shift(LEFT*3.5)
        cText = Text("c", font_size=30).next_to(hcg1['radius_line'], UP).set_color(RED)
        self.play(TransformMatchingTex(hX1, hX2), TransformMatchingTex(hY1, hY2),
                TransformMatchingTex(eX1, eX2), TransformMatchingTex(eY1, eY2),
                TransformMatchingShapes(rText, cText))

        self.wait()
        self.play(ReplacementTransform(hcg1, hcg2))
        self.wait()
        self.play(ReplacementTransform(hcg2, hcg3))
        self.wait()
        self.play(ReplacementTransform(hcg3, hcg1))

        self.wait()
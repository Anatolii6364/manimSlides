from herleitung_epizykloide import *
from manim_slides import Slide

def epicycloid_func(R, r, c, t):
    return np.array([
                (R + r)*np.cos(t) - c*np.cos(((R + r)/r)*t),
                (R + r)*np.sin(t) - c*np.sin(((R + r)/r)*t), 
                0
            ])

def hypocycloid_func(R, r, c, t):
    return np.array([
                (R - r)*np.cos(t) + c*np.cos(((R - r)/r)*t),
                (R - r)*np.sin(t) - c*np.sin(((R - r)/r)*t), 
                0
            ])

def epicycloid(R, r, c, k):
    big = Circle(R, color=WHITE)
    curve = always_redraw(lambda: ParametricFunction(lambda t: 
            epicycloid_func(R, r, c, t),
            color=RED, t_range = np.array([0.001, k.get_value()])).shift(big.get_center()))

    small = Circle(r, color=WHITE)
    small.shift((R+r)*RIGHT)
    small_center = Dot(small.get_center())
    dot = always_redraw(
        lambda: Dot(epicycloid_func(R, r, c, k.get_value())))

    radius_line = always_redraw(lambda: Line(small.get_center(), epicycloid_func(R, r, c, k.get_value()), color=YELLOW))
    return VDict({'radius_line': radius_line,
                  'curve': curve,
                  'big': big, 
                  'small': small,
                  'dot': dot,
                  'small_center': small_center})

def hypocycloid(R, r, c, k):
    big = Circle(R, color=WHITE)
    curve = always_redraw(lambda: ParametricFunction(lambda t: 
            hypocycloid_func(R, r, c, t),
            color=RED, t_range = np.array([0.001, k.get_value()])).shift(big.get_center()))

    small = Circle(r, color=WHITE)
    small.shift((R-r)*RIGHT)
    small_center = Dot(small.get_center())
    dot = always_redraw(
        lambda: Dot(hypocycloid_func(R, r, c, k.get_value())))

    radius_line = always_redraw(lambda: Line(small.get_center(), hypocycloid_func(R, r, c, k.get_value()), color=YELLOW))
    return VDict({'radius_line': radius_line,
                  'curve': curve,
                  'big': big, 
                  'small': small,
                  'dot': dot,
                  'small_center': small_center})

class BasicExample(Slide):

    def construct(self):
        big_r = 3
        small_r = 1

        text_r1 = MathTex("r = 1", color=WHITE).to_edge(UP).to_edge(LEFT)
        text_r2 = MathTex("r = 2/3", color=WHITE).to_edge(UP).to_edge(LEFT)
        text_R1 = MathTex("R = 3", color=WHITE).next_to(text_r1, DOWN).to_edge(LEFT)
        text_R2 = MathTex("R = 2", color=WHITE).next_to(text_r1, DOWN).to_edge(LEFT)
        text_c1 = MathTex("c = 1 \\cdot r", color=WHITE).next_to(text_R1, DOWN).to_edge(LEFT)
        text_c2 = MathTex("c = 0.5 \\cdot r", color=WHITE).next_to(text_R1, DOWN).to_edge(LEFT)
        text_c3 = MathTex("c = 1.5 \\cdot r", color=WHITE).next_to(text_R1, DOWN).to_edge(LEFT)

        text_hypotrochoid = MathTex("Hypotrochoide").to_edge(UP).to_edge(RIGHT)
        text_epitrochoid = MathTex("Epitrochoide").to_edge(UP).to_edge(RIGHT)
        
        
        k = ValueTracker(0.001)
        hc1 = hypocycloid(big_r, small_r, small_r, k)

        self.play(FadeIn(hc1, text_r1, text_R1, text_c1, text_hypotrochoid))
        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(hc1['small'], hc1['small_center']), angle=2*PI, about_point=hc1['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )
        
        self.wait()

        k = ValueTracker(0.001)
        hc2 = hypocycloid(big_r, small_r, 0.5, k)

        self.play(ReplacementTransform(hc1, hc2),
                  TransformMatchingShapes(text_c1, text_c2),
                  )

        self.wait()

        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(hc2['small'], hc2['small_center']), angle=2*PI, about_point=hc2['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )

        self.wait()

        k = ValueTracker(0.001)
        hc3 = hypocycloid(big_r, small_r, 1.5, k)

        self.play(ReplacementTransform(hc2, hc3), TransformMatchingShapes(text_c2, text_c3))

        self.wait()

        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(hc3['small'], hc3['small_center']), angle=2*PI, about_point=hc3['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )
        
        #---------------------- EPI -------------------------
        big_r = 2
        small_r = 2/3

        k = ValueTracker(0.001)
        ec1 = epicycloid(big_r, small_r, small_r, k)

        self.play(ReplacementTransform(hc3, ec1),
                  TransformMatchingShapes(text_r1, text_r2),
                  TransformMatchingShapes(text_c3, text_c1),
                  TransformMatchingShapes(text_hypotrochoid, text_epitrochoid),
                  TransformMatchingShapes(text_R1, text_R2))

        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(ec1['small'], ec1['small_center']), angle=2*PI, about_point=ec1['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )
        
        self.wait()

        k = ValueTracker(0.001)
        ec2 = epicycloid(big_r, small_r, 0.5*small_r, k)

        self.play(ReplacementTransform(ec1, ec2),
                  TransformMatchingShapes(text_c1, text_c2),
                  )

        self.wait()

        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(ec2['small'], ec2['small_center']), angle=2*PI, about_point=ec2['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )

        self.wait()

        k = ValueTracker(0.001)
        ec3 = epicycloid(big_r, small_r, 1.5*small_r, k)

        self.play(ReplacementTransform(ec2, ec3), TransformMatchingShapes(text_c2, text_c3))

        self.wait()

        self.play(
            k.animate.set_value(2*np.pi), 
            Rotate(Group(ec3['small'], ec3['small_center']), angle=2*PI, about_point=ec3['big'].get_center()),
            rate_function=smooth,
            run_time=6
            )
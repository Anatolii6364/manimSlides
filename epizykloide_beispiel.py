from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):

    def construct(self):
        txt_r1 = MathTex("r = 1", color=YELLOW).to_edge(UP).to_edge(LEFT)
        txt_R1 = MathTex("R = 2", color=YELLOW).next_to(txt_r1, DOWN)

        txt_r2 = MathTex("r = 0.5", color=RED).to_edge(UP).to_edge(LEFT)
        txt_R2 = MathTex("R = 2", color=RED).next_to(txt_r1, DOWN)
        
        txt_r3 = MathTex("r = 0.75", color=PURPLE).to_edge(UP).to_edge(LEFT)
        txt_R3 = MathTex("R = 2", color=PURPLE).next_to(txt_r3, DOWN)

        headline = MathTex("Epizykloide").to_edge(UP).to_edge(RIGHT)

        # SLIDE 1
        grid = Axes(
            x_range = (-5, 5),
            y_range = (-4, 4),
            x_length= 12,
            y_length= 7,
            tips=False,
            color=GRAY,
            axis_config={"include_numbers": False})

        big_r = 2
        small_r = 1

        big = Circle(big_r, color=WHITE) 
        small = Circle(small_r, color=WHITE).shift(RIGHT*(big_r+small_r)) 


        k = ValueTracker(0.001)

        curve = always_redraw(lambda: ParametricFunction(lambda t: 
                np.array([
                    (big_r + small_r)*np.cos(t) - small_r*np.cos((-(big_r + small_r)/small_r)*t),
                    (big_r + small_r)*np.sin(t) + small_r*np.sin((-(big_r + small_r)/small_r)*t), 
                    0
                ]),
                color=YELLOW, t_range = np.array([0.001, k.get_value()])))

        trace_dot = always_redraw(lambda: Dot().move_to(
                np.array([
                    (big_r + small_r)*np.cos(k.get_value()) - small_r*np.cos((-(big_r + small_r)/small_r)*k.get_value()),
                    (big_r + small_r)*np.sin(k.get_value()) + small_r*np.sin((-(big_r + small_r)/small_r)*k.get_value()), 
                    0
                ]),
                ))


        self.play(DrawBorderThenFill(grid), DrawBorderThenFill(big), 
                  DrawBorderThenFill(small), Create(trace_dot), FadeIn(headline), FadeIn(txt_r1), FadeIn(txt_R1), run_time=0.6)
        self.wait()

        # SLIDE 3
        self.start_loop()
        self.add(trace_dot)
        self.add(curve)
        self.play(
            k.animate.set_value(2*PI),
            Rotate(small, angle=2*PI, about_point=ORIGIN),
            reate_function=smooth,
            run_time=6
        )
        self.end_loop()
        #--------------------------------------
        big_r = 2
        small_r = 0.5

        big1 = Circle(big_r, color=WHITE) 
        small1 = Circle(small_r, color=WHITE).shift(RIGHT*(big_r+small_r)) 


        n = ValueTracker(0.001)

        curve1 = always_redraw(lambda: ParametricFunction(lambda t: 
                np.array([
                    (big_r + small_r)*np.cos(t) - small_r*np.cos((-(big_r + small_r)/small_r)*t),
                    (big_r + small_r)*np.sin(t) + small_r*np.sin((-(big_r + small_r)/small_r)*t), 
                    0
                ]),
                color=RED, t_range = np.array([0.001, k.get_value()])))

        trace_dot1 = always_redraw(lambda: Dot().move_to(
                np.array([
                    (big_r + small_r)*np.cos(n.get_value()) - small_r*np.cos((-(big_r + small_r)/small_r)*n.get_value()),
                    (big_r + small_r)*np.sin(n.get_value()) + small_r*np.sin((-(big_r + small_r)/small_r)*n.get_value()), 
                    0
                ]),
                ))

        self.play(ReplacementTransform(big,big1), ReplacementTransform(small,small1),
                  ReplacementTransform(trace_dot, trace_dot1), ReplacementTransform(curve, curve1),
                  ReplacementTransform(txt_r1, txt_r2), ReplacementTransform(txt_R1, txt_R2),
                  run_time=0.6)

        self.start_loop()
        self.add(trace_dot1)
        self.add(curve1)
        self.play(
            n.animate.set_value(2*PI),
            Rotate(small1, angle=2*PI, about_point=ORIGIN),
            reate_function=smooth,
            run_time=5
        )
        self.end_loop()

        # #//////////////////////////////////
        big_r1 = 2
        small_r1 = 0.75

        big2 = Circle(big_r1, color=WHITE) 
        small2 = Circle(small_r1, color=WHITE).shift(RIGHT*(big_r1+small_r1)) 

        m = ValueTracker(0.001)

        curve2 = always_redraw(lambda: ParametricFunction(lambda t: 
                np.array([
                    (big_r1 + small_r1)*np.cos(t) - small_r1*np.cos((-(big_r1 + small_r1)/small_r1)*t),
                    (big_r1 + small_r1)*np.sin(t) + small_r1*np.sin((-(big_r1 + small_r1)/small_r1)*t), 
                    0
                ]),
                color=PURPLE, t_range = np.array([0.001, n.get_value()*5])))

        trace_dot2 = always_redraw(lambda: Dot().move_to(
                np.array([
                    (big_r1 + small_r1)*np.cos(m.get_value()) - small_r1*np.cos((-(big_r1 + small_r1)/small_r1)*m.get_value()),
                    (big_r1 + small_r1)*np.sin(m.get_value()) + small_r1*np.sin((-(big_r1 + small_r1)/small_r1)*m.get_value()), 
                    0
                ]),
                ))
        
       

        self.play(ReplacementTransform(small1,small2), ReplacementTransform(big1,big2), 
                  ReplacementTransform(trace_dot1, trace_dot2), ReplacementTransform(curve1, curve2),
                  ReplacementTransform(txt_r2, txt_r3), ReplacementTransform(txt_R2, txt_R3), run_time=0.6)

        self.start_loop()

        self.add(curve2)
        self.play(
            m.animate.set_value(6*PI),
            Rotate(small2, angle=6*PI, about_point=ORIGIN),
            reate_function=smooth,
            run_time=7
        )
        self.end_loop()
        self.wait()
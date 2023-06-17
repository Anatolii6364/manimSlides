from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    def construct(self):

        HEADLINE = Text("Herleitung").scale(1).to_edge(UP)
        self.play(FadeIn(HEADLINE), run_time=0.7)

        big_r = 3
        small_r = 1

        big = Circle(big_r, color=GREY) 
        small = Circle(small_r, color=GREY).shift(RIGHT*1.87).shift(UP*0.7) 


        k = ValueTracker(0.001)

        curve = always_redraw(lambda: ParametricFunction(lambda t: 
                np.array([
                    (big_r - small_r)*np.cos(t) + small_r*np.cos(((big_r - small_r)/small_r)*t),
                    (big_r - small_r)*np.sin(t) - small_r*np.sin(((big_r - small_r)/small_r)*t), 
                    0
                ]),
                color=YELLOW, t_range = np.array([0.001, k.get_value()])))

        trace_dot = always_redraw(lambda: Dot().move_to(
                np.array([
                    (big_r - small_r)*np.cos(k.get_value()) + small_r*np.cos(((big_r - small_r)/small_r)*k.get_value()),
                    (big_r - small_r)*np.sin(k.get_value()) - small_r*np.sin(((big_r - small_r)/small_r)*k.get_value()), 
                    0
                ]),
                ))
        
        
        DL1 = Line(big.get_top(), big.get_bottom(), color="#252626", stroke_width=2)
        DL2 = Line(big.get_left(), big.get_right(), color="#252626",  stroke_width=2)
        # DARROW = DoubleArrow(ORIGIN, small.get_center(), color = RED, tip_length=0.1)
        CP = Dot([2.65,0.1,0], color=YELLOW, radius=0.05)  # Center Point
        CPS = Dot(small.get_center(), color=WHITE, radius=0.05)  # Center Point
        ARROW = Arrow(small.get_center(), CP.get_center(), buff=0.02, tip_length=0.1, stroke_width=4, color="#454545")
        NL = Line([0,0,0], [2.8,1.05,0], color=GRAY)
        ANG = Angle(DL2, NL, radius=0.8, quadrant=(1,1), color="#252626")

        arraye3=[2.65,0.7,0]
        NLS1 = DashedLine(small.get_center(), arraye3, color="#252626")
        NLS2 = DashedLine(arraye3, CP.get_center(), color="#252626")
        RANG = RightAngle(NLS1, NLS2, length=0.1, quadrant=(-1,1), stroke_width=3, color="#252626")

        ANGT = Angle(NLS1, NL, radius=0.7, color="#252626")
        ANGTH = Angle(ARROW, NLS1, radius=0.6, color="#252626")
        ANGTHT = Angle(ARROW, NL, radius=0.5, color="#252626")

        DL3 = Line(small.get_top(), small.get_bottom(), color="#252626", stroke_width=1)
        DL4 = Line(small.get_right(), small.get_left(), color="#252626",  stroke_width=1)


        txt_center = Text("Center:", font_size=20).next_to(HEADLINE, DOWN).shift(RIGHT*4)
        
        hyp_sm_centerx=MathTex("x(t)= (","R-r", ")\\cdot\\cos(", "t" , ")", font_size=25).next_to(txt_center, DOWN)
        hyp_sm_centerx[1].set_color(ORANGE)
        hyp_sm_centerx[3].set_color(BLUE)
        
        hyp_sm_centery=MathTex("y(t)= (","R-r", ")\\cdot\\sin(","t",")", font_size=25).next_to(hyp_sm_centerx, DOWN)
        hyp_sm_centery[1].set_color(ORANGE)
        hyp_sm_centery[3].set_color(BLUE)

        txt_trace = Text("Trace Point: ", font_size=20).next_to(hyp_sm_centery, DOWN)
        
        hyp_sm_tracex=MathTex("x(t)= (","R-r", ")\\cdot\\cos(", "t",") +","r", "\\cdot\\cos(\\","\\theta-t",")", font_size=25).next_to(txt_trace, DOWN)
        hyp_sm_tracex[1].set_color(ORANGE)
        hyp_sm_tracex[3].set_color(BLUE)
        hyp_sm_tracex[5].set_color(YELLOW)
        hyp_sm_tracex[7].set_color(GREEN)


        hyp_sm_tracey=MathTex("y(t)= (","R-r",")\\cdot\\sin(","t",") - ", "r", "\\cdot\\sin(\\","\\theta-t",")", font_size=25).next_to(hyp_sm_tracex, DOWN)
        hyp_sm_tracey[1].set_color(ORANGE)
        hyp_sm_tracey[3].set_color(BLUE)
        hyp_sm_tracey[5].set_color(YELLOW)
        hyp_sm_tracey[7].set_color(GREEN)


        derivation = MathTex("r\\theta = Rt \\Rightarrow \\theta = \\frac{Rt}{r}", font_size=25).next_to(hyp_sm_tracey, DOWN)
        derivation2 = MathTex("\\theta-t = \\frac{Rt}{r}-t\\cdot\\frac{r}{r}=\\frac{R-t}{r}\\cdot t", font_size=25).next_to(derivation, DOWN)

        txt_parametric = Text("Parametric Hypocycloid: ", font_size=20).next_to(derivation2, DOWN)
        hyper_zx=MathTex("x(t)= ","(R-r)\\cdot\\cos(t)", "+", "r\\cdot\\cos(\\frac{R-r}{r}\\cdot t)",font_size=25).next_to(txt_parametric, DOWN)
        hyper_zy=MathTex("y(t)= ","(R-r)\\cdot\\sin(t)", "-", "r\\cdot\\sin(\\frac{R-r}{r}\\cdot t)", font_size=25).next_to(hyper_zx, DOWN)


        letter_R=MathTex("R", font_size=25, color="#252626").next_to(NL).shift(LEFT*1.8).shift(DOWN*0.2)
        letter_r=MathTex("r", font_size = 25, color="#252626").next_to(ARROW, LEFT).shift(RIGHT*0.58).shift(DOWN*0.2)
        letter_t=MathTex("t", font_size = 20 , color="#252626").shift(RIGHT*0.7).shift(UP*0.13)
        letter_t2=MathTex("t", font_size = 20 , color="#252626").next_to(ANGT, LEFT*0.1)
        letter_theta=MathTex("\\theta-t", font_size = 15, color="#252626").next_to(ANGTH, RIGHT*0.01).shift(DOWN*0.1)
        
        letter_tht = MathTex("\\theta", font_size=20, color="#252626").next_to(ANGTHT, LEFT*0.1).shift(DOWN*0.05).shift(RIGHT*0.06)

        
        RP = VGroup(letter_R, letter_t, letter_r, letter_t2, letter_theta, letter_tht).shift(DOWN*0.6)
        RV = VGroup( ANGT, ANGTH, NLS1, NLS2, ANGTHT, ANG, NL, CP, ARROW, CPS, RANG).shift(DOWN*0.6)
        RC = VGroup(DL1, DL2, big,  DL3, DL4, small, ).shift(DOWN*0.6)

        ALL = VGroup(RC, RV, RP)

        self.play(Create(RC), Create(RV), FadeIn(RP), run_time=0.8)


        # Scale animation
        self.play(ALL.animate.scale(2.2),run_time=0.7)
        self.play(ALL.animate.shift(DOWN*2.2 + LEFT*6.5), run_time=0.7)
        self.wait()

        # Center Formula
        BRACE = BraceBetweenPoints( small.get_center(), DL1.get_center(), buff=0, color = "#252626")
        letter_Rr=MathTex("R-r", font_size = 40, color="#252626").next_to(BRACE, UP*0.01).shift(DOWN*0.5).shift(LEFT*0.2)
        self.play(FadeIn(txt_center),BRACE.animate.set_color(ORANGE), letter_Rr.animate.set_color(ORANGE), 
                  NL.animate.set_color(WHITE), letter_R.animate.set_color(WHITE), 
                  ANG.animate.set_color(BLUE), letter_t.animate.set_color(BLUE), 
                  FadeIn(hyp_sm_centerx), FadeIn(hyp_sm_centery))
        
        self.wait()

        # Trace Formula
        self.play(FadeIn(txt_trace), 
                  NL.animate.set_color("#dddddd"), letter_R.animate.set_color("#dddddd"),
                  ARROW.animate.set_color(WHITE), letter_r.animate.set_color(WHITE),     
                  ANGT.animate.set_color(BLUE), letter_t2.animate.set_color(BLUE),
                  NLS1.animate.set_color(GREY), NLS2.animate.set_color(GREY),     
                  RANG.animate.set_color(GREY), letter_theta.animate.set_color(GREEN),
                  letter_tht.animate.set_color(RED), ANGTH.animate.set_color(GREEN), 
                  ANGTHT.animate.set_color(RED),FadeIn(hyp_sm_tracex), FadeIn(hyp_sm_tracey))
    
        self.wait()
        
        # Derivation
        self.play(FadeIn(derivation), FadeIn(derivation2))

        self.wait()
        self.play(FadeIn(txt_parametric),FadeIn(hyper_zx), FadeIn(hyper_zy))

        
        
        self.wait(2)



        




        # self.play(Write(theta.next_to(RC, DOWN)))

        # framebox1 = SurroundingRectangle(base_x[2], buff = .1, color="WHITE")
        # framebox2 = SurroundingRectangle(base_y[2], buff = .1, color="WHITE")
        # self.play(Create(framebox1), Create(framebox2))
        
        # self.wait()

        # brace = BraceBetweenPoints(C.get_bottom(), C.get_center(), color="#00ffdd")
        # txt_one = MathTex("1").next_to(brace, RIGHT)
        # self.play(Create(brace), Create(txt_one))

        self.wait()



        
















































        # grid = NumberPlane(axis_config={"include_numbers": True})

        # big_r = 3
        # # small_r = 1

        # big = Circle(big_r, color=WHITE) 
        # # small = Circle(small_r, color=WHITE).shift(RIGHT*(big_r-small_r)) 

        # k = ValueTracker(0.001)

        # curve = always_redraw(lambda: ParametricFunction(lambda t: 
        #         np.array([
        #             # (big_r - small_r)*np.cos(t) + small_r*np.cos(((big_r - small_r)/small_r)*t),
        #             # (big_r - small_r)*np.sin(t) - small_r*np.sin(((big_r - small_r)/small_r)*t), 
        #             big_r*(t - np.sin(t)),
        #             big_r*(1 - np.cos(t)), 
        #             0
        #         ]),
        #         color=RED, t_range = np.array([0.001, k.get_value()])))

        # trace_dot = always_redraw(lambda: Dot().move_to(
        #         np.array([
        #             # (big_r - small_r)*np.cos(k.get_value()) + small_r*np.cos(((big_r - small_r)/small_r)*k.get_value()),
        #             # (big_r - small_r)*np.sin(k.get_value()) - small_r*np.sin(((big_r - small_r)/small_r)*k.get_value()), 
        #             big_r*(k.get_value() - np.sin(k.get_value())),
        #             big_r*(1 - np.cos(k.get_value())),
        #             0
        #         ]),
        #         ))


        # self.play(DrawBorderThenFill(grid), DrawBorderThenFill(big))
        # self.next_slide()

        # # SLIDE 3
        # self.start_loop()
        # self.add(trace_dot)
        # self.add(curve)
        # self.play(
        #     k.animate.set_value(2*PI),
        #     Rotate(big, angle=2*PI, about_point=ORIGIN),
        #     reate_function=smooth,
        #     run_time=5
        # )

        # self.end_loop()
        # self.wait(1)
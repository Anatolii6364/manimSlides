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
        
        letter_tht = MathTex("\\theta", font_size=20, color="#252626").next_to(ANGTHT, LEFT*0.1).shift(DOWN*0.01).shift(RIGHT*0.06)

        
        RP = VGroup(letter_R, letter_t, letter_r, letter_t2, letter_theta, letter_tht).shift(DOWN*0.6)
        RV = VGroup(ANGT, ANGTH, NLS1, NLS2, ANGTHT, ANG, NL, CP, ARROW, CPS, RANG).shift(DOWN*0.6)
        RC = VGroup(DL1, DL2, big,  DL3, DL4, small, ).shift(DOWN*0.6)

        ALL = VGroup(RC, RP, RV)

        self.play(Create(RC), Create(RV), FadeIn(RP), run_time=0)



        # Scale animation
        self.play(ALL.animate.scale(2.2),run_time=0)
        self.play(ALL.animate.shift(DOWN*2.2 + LEFT*6.5), run_time=0)

        BRACE = BraceBetweenPoints( small.get_center(), DL1.get_center(), buff=0, color = "#252626")
        letter_Rr=MathTex("R-r", font_size = 40, color="#252626").next_to(BRACE, UP*0.01).shift(DOWN*0.5).shift(LEFT*0.2)

        # Center Formula
        self.play(FadeIn(txt_center),BRACE.animate.set_color(ORANGE), letter_Rr.animate.set_color(ORANGE), 
                  NL.animate.set_color(WHITE), letter_R.animate.set_color(WHITE), 
                  ANG.animate.set_color(BLUE), letter_t.animate.set_color(BLUE), 
                  FadeIn(hyp_sm_centerx), FadeIn(hyp_sm_centery), run_time=0)
        

        # Trace Formula
        self.play(FadeIn(txt_trace), 
                  NL.animate.set_color("#dddddd"), letter_R.animate.set_color("#dddddd"),
                  ARROW.animate.set_color(WHITE), letter_r.animate.set_color(WHITE),     
                  ANGT.animate.set_color(BLUE), letter_t2.animate.set_color(BLUE),
                  NLS1.animate.set_color(WHITE), NLS2.animate.set_color(WHITE),     
                  RANG.animate.set_color(WHITE), letter_theta.animate.set_color(GREEN),
                  letter_tht.animate.set_color(RED), ANGTH.animate.set_color(GREEN), 
                  ANGTHT.animate.set_color(RED),FadeIn(hyp_sm_tracex), FadeIn(hyp_sm_tracey), run_time=0)
    
        # Derivation
        self.play(FadeIn(derivation), FadeIn(derivation2), run_time=0)

        self.play(FadeIn(txt_parametric),FadeIn(hyper_zx), FadeIn(hyper_zy), run_time=0)
        self.wait()
        

        ################################################################### TEIL 2


        big_r = 2.5 
        small_r = 1

        biga = Circle(big_r, color=GREY) 
        smalla = Circle(small_r, color=GREY).shift(RIGHT*(big_r+small_r)*np.cos(np.pi/4)).shift(UP*(big_r+small_r)*np.sin(np.pi/4)) 

        DL1A = Line(biga.get_top(), biga.get_bottom(), color="#252626", stroke_width=2)
        DL2A = Line(biga.get_left(), biga.get_right(), color="#252626",  stroke_width=2)
        # DARROW = DoubleArrow(ORIGIN, small.get_center(), color = RED, tip_length=0.1)

        CPA = Dot(np.array(smalla.get_center())+np.array([small_r*np.cos(-1/8*np.pi), small_r*np.sin(-1/8*np.pi), 0]), color=YELLOW, radius=0.05)  # Center Point

        CPSA = Dot(smalla.get_center(), color=WHITE, radius=0.05)  # Center Point
        ARROWA = Arrow(smalla.get_center(), CPA.get_center(), buff=0.02, tip_length=0.1, stroke_width=4, color="#454545")
        NLA = Line(biga.get_center(), smalla.get_center(), color=GRAY)
        ANGA = Angle(DL2A, NLA, radius=1, quadrant=(1,1), color="#252626")

        arraye3=[2.65,0.7,0]
        NLS1A = Line(smalla.get_center(), smalla.get_center()-RIGHT*small_r, color="#252626")
        NLS2A = Line(smalla.get_center()-RIGHT*small_r, CPA.get_center(), color="#252626").set_opacity(0)
        RANGA = RightAngle(NLS1A, NLS2A, length=0.1, quadrant=(-1,1), stroke_width=3, color="#252626").set_opacity(0)

        ANGTA = Angle(NLS1A, NLA, radius=0.6, quadrant=(1,-1), color="#252626")
        ANGTHA = Angle(NLA, ARROWA, radius=0.4, quadrant=(-1,1), color="#252626")
        ANGTHTA = Angle(NLS1A, ARROWA, radius=0.75, quadrant=(1,1), color="#252626")

        DL3A = Line(smalla.get_top(), smalla.get_bottom(), color="#252626", stroke_width=1)
        DL4A = Line(smalla.get_right(), smalla.get_left(), color="#252626",  stroke_width=1)


        letter_RA=MathTex("R", font_size=30, color="#252626").next_to(NLA, RIGHT*0.1)
        letter_rA=MathTex("r", font_size = 25, color="#252626").next_to(ARROWA, UP*0.1)
        letter_tA=MathTex("t", font_size = 30 , color="#252626").move_to(ANGA.get_center()).shift(LEFT*0.1)
        letter_t2A=MathTex("t", font_size = 20 , color="#252626").move_to(ANGTA.get_center()).shift(RIGHT*0.1)
        letter_thetaA=MathTex("\\theta", font_size = 20, color="#252626").move_to(ANGTHA.get_center())
        
        letter_thtA = MathTex("\\theta+t", font_size=20, color="#252626").move_to(ANGTHTA.get_center()).shift(DOWN*0.2)

        BRACEA = BraceBetweenPoints(smalla.get_center(), DL1A.get_center(), buff=0, color = "#252626")
        BRACE2A = BraceBetweenPoints(smalla.get_center()*(big_r/(big_r+small_r)), biga.get_center(), buff=0, color = WHITE)
        BRACE2A.set_opacity(0.5)
        BRACE2A.rotate(np.pi)
        BRACE2A.put_at_tip(letter_RA, buff=0.1)

        letter_Rra=MathTex("R+r", font_size = 25, color="#252626").next_to(BRACEA, UP).shift(DOWN*1.2).shift(LEFT*0.3)
        RV = VGroup( ANGTA, ANGTHA, NLS1A, BRACEA, NLS2A, ANGTHTA, ANGA, NLA, CPA, ARROWA, CPSA, RANGA, BRACE2A).shift(DOWN*0.6)
        RC = VGroup(DL1A, DL2A, biga,  DL3A, DL4A, smalla, ).shift(DOWN*0.6)
        RP = VGroup(letter_RA, letter_Rra, letter_tA, letter_rA, letter_t2A, letter_thetaA, letter_thtA).shift(DOWN*0.6)

        BRACEA.set_color(ORANGE).set_opacity(0.5)
        letter_Rra.set_color(ORANGE)
        NLA.set_color(WHITE)
        letter_RA.set_color(WHITE)
        ANGA.set_color(BLUE)
        letter_tA.set_color(BLUE)
        
        self.wait()

        # Trace Formula
        NLA.set_color("#dddddd")
        letter_RA.set_color("#dddddd")
        ARROWA.set_color(WHITE)
        letter_rA.set_color(WHITE)
        ANGTA.set_color(BLUE)
        letter_t2A.set_color(BLUE)
        NLS1A.set_color(WHITE)
        NLS2A.set_color(WHITE)     
        RANGA.set_color(WHITE)
        letter_thetaA.set_color(RED)
        letter_thtA.set_color(GREEN)
        ANGTHA.set_color(RED), 
        ANGTHTA.set_color(GREEN)

        ALL2 = VGroup(RC, RP, RV)


        ALL2.scale(1.5)
        ALL2.shift(DOWN*2.0 + LEFT*5)


        self.play(Transform(big, biga),
                  Transform(small, smalla),
                  Transform(DL1, DL1A),
                  Transform(DL2, DL2A),
                  Transform(DL3, DL3A),
                  Transform(DL4, DL4A),
                  Transform(CP, CPA),
                  Transform(CPS, CPSA),
                  Transform(NLS1, NLS1A),
                  Transform(NLS2, NLS2A),
                  Transform(NL, NLA),
                  Transform(ANG, ANGA),
                  Transform(ANGT, ANGTA),
                  Transform(ANGTH, ANGTHA),
                  Transform(ANGTHT, ANGTHTA),
                  Transform(RANG, RANGA),
                  Transform(ARROW, ARROWA),
                  Transform(letter_Rr, letter_Rra),
                  Transform(BRACE, BRACEA),
                  Transform(letter_R, letter_RA),
                  Transform(letter_r, letter_rA),
                  Transform(letter_t, letter_tA),
                  Transform(letter_tht, letter_thtA),
                  Transform(letter_t2, letter_t2A),
                  Transform(letter_theta, letter_thetaA),
                  FadeIn(BRACE2A),
                  FadeOut(txt_center),
                  FadeOut(hyp_sm_centerx),
                  FadeOut(hyp_sm_centery),
                  FadeOut(hyp_sm_tracex),
                  FadeOut(hyp_sm_tracey),
                  FadeOut(txt_trace),
                  FadeOut(hyper_zx),
                  FadeOut(hyper_zy),
                  FadeOut(derivation),
                  FadeOut(derivation2),
                  FadeOut(txt_parametric))
        self.wait()
        textX1=MathTex("x(t)= (", "R+r", ") \\cdot\\cos(t)",font_size=30).shift(RIGHT*3.5 + UP)
        textY1=MathTex("y(t)= (", "R+r", ") \\cdot\\sin(t)", font_size=30).next_to(textX1, DOWN)

        textX1[1].set_color(ORANGE)
        textY1[1].set_color(ORANGE)

        self.play(FadeIn(textX1, textY1))

        self.wait()

        textX2=MathTex("x(t)= (", "R+r", ")\\cdot\\cos(t)", "-", "r\\cdot\\cos(", "\\theta+t", "})",font_size=30).shift(RIGHT*3.5 + UP)
        textY2=MathTex("y(t)= (", "R+r", ")\\cdot\\sin(t)", "-", "r\\cdot\\sin(", "\\theta+t", "})", font_size=30).next_to(textX2, DOWN)

        textX2[1].set_color(ORANGE)
        textY2[1].set_color(ORANGE)
        textX2[5].set_color(GREEN)
        textY2[5].set_color(GREEN)

        self.play(TransformMatchingTex(textX1, textX2),
                  TransformMatchingTex(textY1, textY2)
                  )

        self.wait()

        derivation1 = MathTex("r\\theta = Rt", "\\Rightarrow", "\\theta = \\frac{Rt}{r}", font_size=25).next_to(textY2, DOWN)
        derivation2 = MathTex("\\theta+t", "= ", "\\frac{Rt}{r}+t", font_size=25).next_to(derivation1, DOWN)

        self.play(FadeIn(derivation1))
        self.wait()
        self.play(FadeIn(derivation2))
        self.wait()
        derivation3 = MathTex("\\theta+t",  "=", "\\frac{Rt}{r} + \\frac{t\\cdot r}{r}", font_size=25).next_to(derivation1, DOWN)
        self.wait()
        self.play(TransformMatchingTex(derivation2, derivation3))
        self.wait()
        derivation4 = MathTex("\\theta+t",  "=", "\\frac{R+r}{r}\\cdot t", font_size=25).next_to(derivation1, DOWN)
        self.play(TransformMatchingTex(derivation3, derivation4))
        self.wait()
        derivation5 = MathTex("\\theta+t",  "=", "\\frac{R+r}{r}\\cdot t", font_size=25).next_to(derivation1, DOWN).set_color(GREEN)
        derivation5[1].set_color(WHITE)
        self.play(TransformMatchingTex(derivation4, derivation5))
        self.wait()
        textX3=MathTex("x(t)= (", "R+r", ")\\cdot\\cos(t)", "-", "r\\cdot\\cos\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)",font_size=30).shift(RIGHT*3.5 + UP)
        textY3=MathTex("y(t)= (", "R+r", ")\\cdot\\sin(t)", "-", "r\\cdot\\sin\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)", font_size=30).next_to(textX2, DOWN)
        textX3[1].set_color(ORANGE)
        textY3[1].set_color(ORANGE)
        textX3[5].set_color(GREEN)
        textY3[5].set_color(GREEN)

        self.play(TransformMatchingTex(Group(derivation5, textX2, textY2), Group(textX3, textY3)), FadeOut(derivation1))
        self.wait()

        textX4=MathTex("x(t)= (", "R+r", ")\\cdot\\cos(t)", "-", "r\\cdot\\cos\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)",font_size=30).shift(RIGHT*3.5 + UP)
        textY4=MathTex("y(t)= (", "R+r", ")\\cdot\\sin(t)", "-", "r\\cdot\\sin\\left(", "\\frac{R+r}{r}\\cdot t", "\\right)", font_size=30).next_to(textX2, DOWN)
        textX4[1].set_color(ORANGE)
        textY4[1].set_color(ORANGE)
        textX4[5].set_color(GREEN)
        textY4[5].set_color(GREEN)

        self.play(TransformMatchingTex(Group(textX3, textY3), Group(textX4, textY4)))

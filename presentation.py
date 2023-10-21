from manim import *
from manim_slides import Slide

class introducao(Slide):
    def construct(self):
        self.camera.background_color = "#1c1c1c"

        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        #==================== Start Pause ====================
        self.wait(0.1)
        self.next_slide()
        
        #==================== Titulo ====================
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_white = "#ffffff"
        
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_white).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)


        introduc1 = Text("Introdução ao Manim",font_size=52)
        introduc2 = Text("Math Animation Engine",font_size=40,slant=ITALIC)
        introduc2.next_to(introduc1,DOWN)

        introduc_text = VGroup(introduc1,introduc2)
        

        self.play(Write(logo))
        self.wait(0.1)
        self.play(logo.animate.shift(UP))
        introduc_text.next_to(logo,DOWN)
        self.play(Write(introduc_text))
        self.next_slide()
       
        #==================== O que é Manim ? ====================
        self.play(FadeOut(logo),FadeOut(introduc_text))       

        text1 = Text("O que é Manim ?")
        text1_1 = Tex("\\justifying {Manim é uma biblioteca Python, feita para criar animações programáticas com foco em assuntos matemáticos.}",
                      tex_template=myBaseTemplate).scale(0.8)

        self.play(Write(text1))
        self.next_slide()

        self.play(text1.animate.shift((UP*3)+(LEFT*4)))
        text1_1.shift(UP*2)

        self.play(Write(text1_1))
        self.next_slide()
        
        #==================== Codico com animação ====================
        code1 = Code(
        "Example1.py",
        tab_width=2,
        background_stroke_width=1,
        background_stroke_color=WHITE,
        insert_line_no=True,
        style=Code.styles_list[15],
        background="rectangle",
        language="python",
        ).scale(0.8)
        code1.shift((LEFT*3)+(DOWN))
       
        self.play(Write(code1))
        self.next_slide()

        circle = Circle(color=ORANGE)
        circle.set_fill(ORANGE, opacity=0.5)
        circle.next_to(code1,RIGHT)
        circle.shift(RIGHT*2)
        
        arrow = Arrow(code1.get_center(),circle)
        arrow.z_index = -1

        self.play(Create(arrow))
        self.wait(0.5)
        self.play(Create(circle))            
        self.wait(0.1)
        self.next_slide()

        #==================== Exemplo com Latex ====================
        code2 = Code(
        "Example1_1.py",
        tab_width=2,
        background_stroke_width=1,
        background_stroke_color=WHITE,
        insert_line_no=True,
        style=Code.styles_list[15],
        background="rectangle",
        language="python",
        ).scale(0.8)
        code2.move_to(code1.get_center())
        
        self.play(FadeOut(text1_1),FadeOut(arrow),Transform(code1,code2),FadeOut(circle))
        self.wait(0.1)
        self.next_slide()
        
        latex = MathTex("4^2 &= x^2 + x^2\\\\",
                        "16 &= 2x^2\\\\",
                        "\\frac{16}{2} &= x^2\\\\",
                        "8 &= x^2\\\\",
                        "x &= \\sqrt{8}\\\\",
                        "x &= 2 \\sqrt{2}\\\\")
        
        latex2 = MathTex(r"4^2 &= x^2 + x^2\\",
                        r"16 &= 2x^2\\",
                        r"\frac{16}{2} &= x^2\\",
                        r"8 &= x^2\\",
                        r"x &= \sqrt{8}\\",
                        r"x &= 2 \sqrt{2}\\",
                        substrings_to_isolate="x")
        
        latex.next_to(code2,RIGHT)
        latex.shift(RIGHT*2)
        latex2.move_to(latex.get_center())

        latex.shift(UP*(1/2))
        latex2.shift(UP*(1/2))
        
        for i in range(0,6):
            self.play(Write(latex[i]))
            self.wait(0.1)
            self.next_slide()
            
        code3 = Code(
        "Example1_2.py",
        tab_width=2,
        background_stroke_width=1,
        background_stroke_color=WHITE,
        insert_line_no=True,
        style=Code.styles_list[15],
        background="rectangle",
        language="python",
        ).scale(0.8)
        code3.move_to(code1.get_center())
        code3.shift(UP*(1/2))
        
        self.play(Transform(code1,code3))
        self.next_slide()
        
        latex2.set_color_by_tex("x", RED)
        self.play(FadeIn(latex2),FadeOut(latex))
        self.next_slide()
        
        # Apagando tudo
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.next_slide()
        
        #==================== De onde surgiu o Manim ? ====================
        text2 = Text("De onde surgiu o Manim ?")

        self.play(Write(text2))
        self.next_slide()


        self.play(text2.animate.shift((UP*3)))
        self.next_slide()   

        
        grant_image = ImageMobject("assets\grant_sanderson.png").scale(0.5)
        grant_image.move_to(ORIGIN)
        
        grant_text = Text("Grant Sanderson").scale(0.6)
        grant_text.next_to(grant_image,DOWN)
       
        self.play(FadeIn(grant_image),FadeIn(grant_text))
        self.play(grant_image.animate.shift(LEFT*3),grant_text.animate.shift(LEFT*3))
        self.next_slide()


        yt_grant_logo = SVGMobject(r"assets\3B1B_Logo.svg").scale(1.1)
        yt_name = Text("3Blue1Brown").scale(0.6)
        yt_logo = SVGMobject("assets\youtube-svgrepo-com.svg").scale(0.3).next_to(yt_name,LEFT)

        underline = VGroup(yt_name,yt_logo)
        underline.next_to(yt_grant_logo,DOWN)

        rightasset = VGroup(yt_grant_logo,underline)

        rightasset.shift(RIGHT)
        self.play(FadeIn(rightasset),rightasset.animate.shift(RIGHT*2))
        self.next_slide()

        # Apagando tudo
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.next_slide()

        #==================== Primeiros passos: Como instalar o Manim ? ====================
        text3 = Text("Primeiros passos: Como instalar o Manim ?")

        self.play(Write(text3))
        self.next_slide()

        self.play(text3.animate.shift((UP*3.3)))
        self.next_slide()


        python_logo = ImageMobject("assets\Python-logo-notext.svg.png")
        miktext_logo = ImageMobject("assets\miktexlogo.png")
        visual_logo = ImageMobject("assets\VS_Code_logo.png")
        ffmpeg_logo = ImageMobject(r"assets\1280px-FFmpeg-Logo.png")

        python_logo.shift(UL+LEFT)
        miktext_logo.shift(UR+RIGHT)
        ffmpeg_logo.shift(DR*2)
        visual_logo.shift(DL*2)

        self.play(FadeIn(python_logo))
        self.next_slide()

        self.play(FadeIn(miktext_logo))
        self.next_slide()
       
        self.play(FadeIn(ffmpeg_logo))
        self.next_slide()
        
        self.play(FadeIn(visual_logo))
        self.next_slide()        
        
        # Apagando tudo
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.next_slide()
        
        
        
#==================== Como as cores funcionam ====================
class cores(Slide):
    def construct(self):
        self.camera.background_color = "#1c1c1c"

        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")  



        




        

#==================== Movimentação e Posição ====================
class movimentacao_e_posicao(Slide):
    def construct(self):
        pass



from manim import *
from manim_slides import Slide

class introducao(Slide):
    def construct(self):
        self.camera.background_color = "#242424"

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
        














class exemplo1(Slide):
    def construct(self):
        code1 = Code(
        "Example1.py",
        tab_width=2,
        background_stroke_width=1,
        background_stroke_color=WHITE,
        insert_line_no=True,
        style=Code.styles_list[15],
        background="rectangle",
        language="python",
        )
        
        self.play(Write(code1))   
        self.next_slide()


class exemplo2(Slide):
    def construct(self):
        pass



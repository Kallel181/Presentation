from manim import *
 
class Figuras(Scene):
    def construct(self):
        circulo = Circle(color=RED)
        self.play(Create(circulo))
        self.wait(1)
 
        quadrado = Square()
        quadrado.set_color(BLUE)
        quadrado.set_fill(color=BLUE,opacity=0.2)
        quadrado.move_to([0,-2.5,0])
        self.play(Create(quadrado))
        self.wait(1)
   
        tri = Triangle(color=GREEN)
        tri.set_fill(color=GREEN,opacity=0.7)
        tri.move_to([0,2.5,0])
        self.play(FadeIn(tri))
        self.wait(1)

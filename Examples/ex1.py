from manim import *
 
class Circulo(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(ORANGE, opacity=0.5)
        self.play(Create(circle))

from manim import *
from manim_slides import Slide
 
class Circulo(Slide):
    def construct(self):
        latex = MathTex("4^2 &= x^2 + x^2\\\\",
                        "16 &= 2x^2\\\\",
                        "\\frac{16}{2} &= x^2\\\\",
                        "8 &= x^2\\\\",
                        "x &= \\sqrt{8}\\\\",
                        "x &= 2 \\sqrt{2}\\\\")
        
        for i in range(0,6):
            self.play(Write(latex[i]))
            self.wait(0.1)
            self.next_slide()
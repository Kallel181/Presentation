from manim import *
from manim_slides import Slide
 
class Circulo(Slide):
    def construct(self):
        latex = MathTex(r"4^2 &= x^2 + x^2\\",
                        r"16 &= 2x^2\\",
                        r"\frac{16}{2} &= x^2\\",
                        r"8 &= x^2\\",
                        r"x &= \sqrt{8}\\",
                        r"x &= 2 \sqrt{2}\\",
                        substrings_to_isolate="x")
        
        for i in range(0,6):
            self.play(Write(latex[i]))
            self.wait(0.1)
            self.next_slide()
        
        latex.set_color_by_tex("x", RED)
        self.play(Transform(latex,latex))
        self.next_slide()
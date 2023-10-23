from manim import *
from manim_slides import Slide
 
class exercicio(Slide):
  def construct(self):
    figura = VGroup()
    #===== Desenhar o círculo e indicar seu raio =====
    raio_circ = 2
    lado_quadrado = 2*raio_circ/(2**(1/2))
 
    circulo = Circle(radius=raio_circ,color=BLUE)
    linha_raio = Line([0,0,0],[lado_quadrado/2,-lado_quadrado/2,0],color=BLUE)
 
    raio = MathTex(str(raio_circ),color=BLUE)
    raio.move_to(linha_raio.get_center())
    raio.shift(UR*(1/4))
 
    self.play(Create(circulo))
    self.wait(0.1)
    self.next_slide()
 
    self.play(Create(linha_raio)) 
    self.play(Write(raio))
    self.wait(0.1)
    self.next_slide()
 
    figura.add(circulo,raio,linha_raio)
     
    #===== Desenhar o quadrado =====
    quadrado = Square(side_length=lado_quadrado*0.98,color=GREEN)
     
    self.play(Create(quadrado))
    self.wait(0.1)
    self.next_slide()    
 
    figura.add(quadrado)       
     
    #===== Evidenciar a diferença entre a área do círculo e a área do quadrado =====
    diferenca = Exclusion(circulo, quadrado, fill_opacity=0.4,color=BLUE)
    diferenca.z_index = -1
 
    self.play(FadeIn(diferenca))
    self.wait(0.1)
    self.next_slide() 
 
    figura.add(diferenca)
     
    #===== Copiar o segmento de reta que indica o raio do círculo e rotacionar para indicar o diâmetro do círculo =====
    linha_raio2 = linha_raio.copy()
    centro = Dot(ORIGIN,color=BLUE)
     
    self.play(FadeIn(centro))
    self.play(Rotate(linha_raio2,angle=PI,about_point=ORIGIN))
    self.wait(0.1)
    self.next_slide() 
 
    figura.add(linha_raio2,centro)
     
    #Copiar raio e mover mais acima
    raio2 = raio.copy()
    raio2.move_to(linha_raio2.get_center())
    raio2.shift(UR*(1/4))
     
    self.play(Write(raio2))
    self.wait(0.1)
    self.next_slide()
 
    figura.add(raio2)
    
    #===== Mover a figura toda para a esquerda =====
    self.play(figura.animate.shift(LEFT*3))
    self.wait(0.1)
    self.next_slide()
 
    #===== A direita vamos usar Pitágoras para encontrar o lado do quadrado =====
 
    #Evidenciar na figura o lado do quadrado
    lado1 = MathTex("x",color=GREEN)
    lado1.move_to(centro.get_center())
    lado1.shift(LEFT)
 
    lado2 = lado1.copy()
    lado2.move_to(centro.get_center())
    lado2.shift(DOWN)
 
    self.play(Write(lado1),Write(lado2))
    self.wait(0.1)
    self.next_slide()
 
    #Adicionando as contas
    pitagoras = MathTex("4^2 &= x^2 + x^2\\\\",
                        "16 &= 2x^2\\\\",
                        "\\frac{16}{2} &= x^2\\\\",
                        "8 &= x^2\\\\",
                        "x &= \\sqrt{8}\\\\",
                        "x &= 2 \\sqrt{2}\\\\")
     
    pitagoras.shift(RIGHT*3)
     
    for i in range(0,6):
      self.play(Write(pitagoras[i]))
      self.wait(0.1)
      self.next_slide()
 
    #trocar x da figura pelo resultado da conta
    self.play(FadeOut(lado1))
 
    result_lado_quadrado = MathTex("2 \\sqrt{2}",color=GREEN,font_size=40)
    result_lado_quadrado.move_to(lado2.get_center())
 
    self.play(Transform(lado2,result_lado_quadrado))
    self.wait(0.1)
    self.next_slide()
 
    #===== Apagar as contas para o lado do quadrado =====
    self.play(FadeOut(pitagoras))
    self.wait(0.1)
    self.next_slide()
 
    #===== Calcular a area do Circulo =====
    circ_area = MathTex("A_c", "&= \\pi r^2 \\\\",
                        "A_c &= 4 \\pi")
 
    circ_area.move_to(ORIGIN)
    circ_area.shift(RIGHT*3)
 
    self.play(Write(circ_area[0]),Write(circ_area[1]))
    self.wait(0.1)
    self.next_slide()    
     
    #Evidenciar a area do circulo na figura
    circulo2 = circulo.copy()
    circulo2.set_fill(opacity=0.3,color=BLUE)
    circulo2.z_index = -5
 
    self.play(FadeOut(diferenca),FadeOut(quadrado),FadeOut(lado2),FadeOut(linha_raio2),FadeOut(raio2))
    self.wait(0.1)
    self.next_slide()
     
    self.play(FadeToColor(circ_area[0],color=BLUE),Create(circulo2))
    self.wait(0.1)
    self.next_slide()
 
    #continuar a conta
    self.play(Write(circ_area[2]))
    self.wait(0.1)
    self.next_slide()
 
    #retornar a figura
    self.play(FadeIn(diferenca),FadeIn(quadrado),FadeIn(lado2),FadeIn(linha_raio2),FadeIn(raio2),FadeOut(circulo2))
    self.wait(0.1)
    self.next_slide()
 
    #reservando o resultado mais acima
    circ_area_resul = circ_area[2].copy()
    circ_area_resul.shift(UP*3)
    circ_area_resul.shift(LEFT)
 
    self.play(Transform(circ_area,circ_area_resul))
    self.wait(0.1)
    self.next_slide()
 
    #==== Calculando a area do quadrado =====
    quad_area = MathTex("A_q", "&= l^2 \\\\",
                        "A_q &= (2\\sqrt{2})^2\\\\",
                        "A_q &= 8")
 
    quad_area.move_to(ORIGIN)
    quad_area.shift(RIGHT*3)
 
    self.play(Write(quad_area[0]),Write(quad_area[1]))
    self.wait(0.1)
    self.next_slide()  
 
    #Evidenciar a area do quadrado na figura
    quadrado2 = quadrado.copy()
    quadrado2.set_fill(opacity=0.3,color=GREEN)
    quadrado2.z_index = -5
 
    self.play(FadeOut(diferenca),FadeOut(circulo),FadeOut(raio),FadeOut(raio2),FadeOut(linha_raio2),FadeOut(linha_raio),FadeOut(raio),FadeOut(centro))
    self.wait(0.1)
    self.next_slide()
 
    self.play(FadeToColor(quad_area[0],color=GREEN),Create(quadrado2))
    self.wait(0.1)
    self.next_slide()
 
    #continuar a conta
    self.play(Write(quad_area[2]))
    self.wait(0.1)
    self.next_slide()
 
    self.play(Write(quad_area[3]))
    self.wait(0.1)
    self.next_slide()
 
    #retornar a figura
    self.play(FadeIn(diferenca),FadeIn(circulo),FadeIn(raio),FadeIn(raio2),FadeIn(linha_raio2),FadeIn(linha_raio),FadeIn(raio),FadeOut(quadrado2),FadeIn(centro))
    self.wait(0.1)
    self.next_slide()
 
    #reservando o resultado mais acima
    quad_area_resul = quad_area[3].copy()
    quad_area_resul.next_to(circ_area_resul,RIGHT)
 
    self.play(Transform(quad_area,quad_area_resul))
    self.wait(0.1)
    self.next_slide()
 
    #===== Calcular a diferença de areas =====
    dif_area = MathTex("A_d &= A_c - A_q\\\\",
                        "A_d &= 4\pi - 8\\\\")
 
    dif_area.move_to(ORIGIN)
    dif_area.shift(RIGHT*3)
 
 
    self.play(Write(dif_area[0]))
    self.wait(0.1)
    self.next_slide()
 
    self.play(Write(dif_area[1]))
    self.wait(0.1)
    self.next_slide()

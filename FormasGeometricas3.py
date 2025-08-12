import turtle  # Importa o módulo turtle para desenhar gráficos na tela

# Classe base para as figuras geométricas

class Figura:

    # Inicializa cor, tamanho e posição da figura
    
    def __init__(self, cor, tamanho, posicao):
        self.cor = cor
        self.tamanho = tamanho
        self.posicao = posicao

    # Método de desenhar padrão que só imprime 10
    
    def desenhar(self):
        print(10)

# Classe que desenha um quadrado, herda de Figura

class Quadrado(Figura):
    
    # Método para desenha quadrado usando o objeto turtle 't'
    
    def desenhar(self, t):
        t.color(self.cor)       # Define a cor da caneta
        t.width(6)              # Define a largura da linha
        t.penup()               # Levanta a caneta para não desenhar ao se mover
        t.goto(self.posicao)    # Move o turtle para a posição inicial da figura
        t.pendown()             # Abaixa a caneta para começar a desenhar
        for _ in range(4):      # Desenha 4 lados do quadrado
            t.forward(self.tamanho)  # Avança o turtle pelo tamanho definido
            t.right(90)               # Vira 90 graus para a direita

# Classe para desenhar um triângulo, herda de Figura

class Triangulo(Figura):
    
    # Método para desenhar o triângulo usando turtle 't'
    
    def desenhar(self, t):
        t.color(self.cor)        # Define cor da caneta
        t.width(6)               # Define largura da linha
        t.penup()                # Levanta caneta para mover sem desenhar
        t.goto(self.posicao)     # Vai para a posição inicial
        t.pendown()              # Abaixa caneta para começar a desenhar
        for _ in range(3):       # Desenha 3 lados do triângulo
            t.forward(self.tamanho)
            t.left(120)          # Vira 120 graus para a esquerda para formar o triângulo

# Classe para desenhar um círculo, herda de Figura

class Circulo(Figura):
    
     # Método para desenhar um círculo usando turtle 't'
     
     def desenhar(self, t):
        t.color(self.cor)        # Define a cor
        t.width(6)               # Define a largura da linha
        t.penup()                # Levanta a caneta para reposicionar
        t.goto(self.posicao)     # Move para a posição inicial
        t.pendown()              # Abaixa a caneta para desenhar
        for _ in range(1):       # Loop único para desenhar o círculo
            t.circle(60)         # Desenha círculo com raio 60

# Classe para desenhar um hexágono, herda de Figura

class Hexagono(Figura):
    
     # Método para desenhar hexágono usando turtle 't'
     
     def desenhar(self, t):
        t.color(self.cor)        # Define cor
        t.width(6)               # Define largura da linha
        t.penup()                # Levanta a caneta para mover
        t.goto(self.posicao)     # Vai para posição inicial
        t.pendown()              # Abaixa caneta para desenhar
        for _ in range(6):       # Desenha 6 lados do hexágono
            t.forward(self.tamanho)
            t.right(60)          # Vira 60 graus para a direita para formar o hexágono

# Cria o objeto turtle para desenhar na tela
t = turtle.Turtle()

# Conta um objeto da classe base Figura (não desenha nada além do print)
fig = Figura("pink",10,(0,0))
fig.desenhar()

# Cria um quadrado rosa tamanho 100 na posição (0, -200) e o desenha
quadrado = Quadrado("pink", 100, (0, -200))
quadrado.desenhar(t)

# Cria um triângulo azul tamanho 120 na posição (200, 0) e o desenha
triangulo = Triangulo("blue", 120, (200, 0))
triangulo.desenhar(t)

# Cria um círculo verde na posição (-200, 0) e o desenha
circulo = Circulo("green", 60, (-200, 0))
circulo.desenhar(t)

# Cria um hexágono roxo na posição (0, 400) e o desenha
hexagono = Hexagono("purple", 60, (0, 400))
hexagono.desenhar(t)

# Mantém a janela aberta até o usuário fechá-la
turtle.done()

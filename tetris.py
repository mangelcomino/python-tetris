import pygame
import random

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana y la matriz
cell_size = 20
matrix_width = 10
matrix_height = 20
#screen_width = cell_size * matrix_width +100
#screen_height = cell_size * matrix_height +100

screen_width=400
screen_height=500

colores=[
    (0,0,0),
    (0,255,255),
    (255,0,0),
    (0,255,0),
    (0,0,255),
    (255,128,0),
    (128,0,128),
    (255,255,0)
]

#Define las piezaS
class Figura:
    figuras =[
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]]
    ]
    def __init__(self,x,y):
        self.x=x
        self.y=y
        i=random.randint(0,len(self.figuras)-1)
        self.tipo=i
        self.color=i+1
        self.rotacion=0
    
    def rotacion_actual(self):
        return self.figuras[self.tipo][self.rotacion]

class Tetris:
    def __init__(self, height, witdh):
        self.height=0
        self.width=0
        self.celda=20
        self.puntos=0
        self.figura_actual=None

        self.height=height
        self.width=witdh
        self.x=100
        self.y=60
        self.tabla=[]
        for i in range(height):
            new_line=[]
            for j in range(witdh):
                new_line.append(0)
            self.tabla.append(new_line)

    def nueva_figura(self):
        self.figura_actual=Figura(3,0)

    def mueve_abajo(self):
        antiguo_y=self.figura_actual.y
        self.figura_actual.y +=1
        if self.choca():
            self.figura_actual.y=antiguo_y
            self.consolida()

    def mueve_lateral(self, dx):
        antiguo_x=self.figura_actual.x
        self.figura_actual.x += dx
        if self.choca():
            self.figura_actual.x=antiguo_x

    
    def rota_pieza(self):
        antigua_rotacion=self.figura_actual.rotacion
        self.figura_actual.rotacion = (self.figura_actual.rotacion+1) % (len(self.figura_actual.figuras[self.figura_actual.tipo]))
        if self.choca():
            self.figura_actual.rotacion=antigua_rotacion

    def choca(self):
        choque=False
        for i in range(4):
            for j in range (4):
                p= i * 4 + j
                if p in self.figura_actual.rotacion_actual():
                    if j+ self.figura_actual.x > self.width-1 or j+self.figura_actual.x<0 or i + self.figura_actual.y > self.height-1 or \
                        self.tabla[i+self.figura_actual.y][j+self.figura_actual.x]>0:
                        choque=True
        return choque
    
    def consolida(self):
        for i in range(4):
            for j in range (4):
                p= i * 4 + j
                if p in self.figura_actual.rotacion_actual():
                    self.tabla[i + self.figura_actual.y][j + self.figura_actual.x] = self.figura_actual.color
        self.nueva_figura()


# Crea la ventana
#screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dibuja la matriz
#for row in range(matrix_height):
#    for col in range(matrix_width):
#        # Calcula las coordenadas de la celda
#        x = col * cell_size +50
#        y = row * cell_size +50
#        # Dibuja el rectángulo de la celda
#        pygame.draw.rect(screen, GRAY, (x, y, cell_size, cell_size))
#        # Dibuja un borde blanco alrededor de la celda
#        pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 1)

# Actualiza la pantalla
#pygame.display.update()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
juego=Tetris(20,10)

# Bucle principal del juego
while True:
    if juego.figura_actual is None:
        juego.nueva_figura()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                juego.mueve_abajo()
            if event.key == pygame.K_LEFT:
                juego.mueve_lateral(-1)
            if event.key == pygame.K_RIGHT:
                juego.mueve_lateral(1)
            if event.key == pygame.K_UP:
                juego.rota_pieza()

                


    screen.fill(WHITE)

    fuente=pygame.font.SysFont('Calibri',25,True,False)
    texto_marcador=fuente.render("Puntos " + str(juego.puntos),True,BLACK)    
    screen.blit(texto_marcador,[0,0])
    #dibujamos la tabla actual
    for i in range(juego.height):
        for j in range(juego.width):
            pygame.draw.rect(screen,GRAY,[juego.x+juego.celda*j, juego.y + juego.celda *i, juego.celda, juego.celda],1)
            if juego.tabla[i][j] > 0:
                pygame.draw.rect(screen,colores[juego.tabla[i][j]],[juego.x + juego.celda*j +1, juego.y + juego.celda * i + 1, juego.celda-2, juego.celda-2])
    #digujamos la pieza actual
    if juego.figura_actual is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in juego.figura_actual.rotacion_actual():
                    pygame.draw.rect(screen,colores[juego.figura_actual.color],
                                     [juego.x + juego.celda * (j + juego.figura_actual.x)+1, juego.y + juego.celda * (i + juego.figura_actual.y)+1,juego.celda-2,juego.celda-2])


    pygame.display.flip()
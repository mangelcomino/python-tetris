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
        self.nivel=1
        self.estado="jugando"

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
        self.chequea_lineas()
        if self.choca()==True:
            self.estado="game over"
        
    def chequea_lineas(self):
        lineas=0
        for i in range(1,self.height):
            ceros=0
            for j in range(self.width):
                if self.tabla[i][j] == 0:
                    ceros+=1
            if ceros == 0:
                lineas+=1
                for i1 in range(i,1,-1):
                    for j in range(self.width):
                        self.tabla[i1][j]=self.tabla[i1-1][j]
        self.puntos+=lineas
        if self.puntos>0:
            self.nivel= (self.puntos // 10) +1

                


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
contador=0
tecla_abajo_presionada=False
tecla_derecha_presionada=False
tecla_izquierda_presionada=False
reloj=pygame.time.Clock()
fps=25

# Bucle principal del juego
while True:
    if juego.figura_actual is None:
        juego.nueva_figura()
    contador +=1
    if contador > 100000:
        contador=0

    if contador % (fps -  juego.nivel*10) == 0 and juego.nivel<10 and juego.estado=="jugando":
        juego.mueve_abajo()
    else:
        if contador % 1 == 0 and juego.nivel>9 and juego.estado=="jugando":
            juego.mueve_abajo()

    if tecla_abajo_presionada==True and contador % 2 ==0 and juego.estado=="jugando":
        juego.mueve_abajo()
    if tecla_derecha_presionada==True and contador % 5 ==0 and juego.estado=="jugando":
        juego.mueve_lateral(1)
    if tecla_izquierda_presionada==True and contador % 5 ==0 and juego.estado=="jugando":
        juego.mueve_lateral(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                #juego.mueve_abajo()
                tecla_abajo_presionada = True
            if event.key == pygame.K_LEFT:
                juego.mueve_lateral(-1)
                tecla_izquierda_presionada = True
            if event.key == pygame.K_RIGHT:
                juego.mueve_lateral(1)
                tecla_derecha_presionada = True
            if event.key == pygame.K_UP:
                juego.rota_pieza()
            if event.key == pygame.K_ESCAPE:
                if juego.estado=="game over":
                    juego.__init__(20,10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                tecla_abajo_presionada = False
            if event.key == pygame.K_LEFT:
                tecla_izquierda_presionada = False
            if event.key == pygame.K_RIGHT:
                tecla_derecha_presionada = False
                


    screen.fill(WHITE)

    fuente=pygame.font.SysFont('Calibri',25,True,False)
    texto_marcador=fuente.render("Puntos " + str(juego.puntos),True,BLACK)
    texto_nivel=fuente.render("Nivel " + str(juego.nivel),True,GRAY)
    texto_game_over =fuente.render("GAME OVER",True,BLACK)    
    screen.blit(texto_marcador,[0,0])
    screen.blit(texto_nivel,[150,0])
    if juego.estado == "game over":
        screen.blit(texto_game_over,[20,200])
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

    reloj.tick(fps)
    pygame.display.flip()
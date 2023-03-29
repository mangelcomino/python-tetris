import pygame

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

class Tetris:
    def __init__(self, height, witdh):
        self.height=0
        self.width=0
        self.celda=20

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    screen.fill(WHITE)

    fuente=pygame.font.SysFont('Calibri',25,True,False)
    texto_marcador=fuente.render("Puntos",True,BLACK)    
    screen.blit(texto_marcador,[0,0])
    for i in range(juego.height):
        for j in range(juego.width):
            pygame.draw.rect(screen,GRAY,[juego.x+juego.celda*j, juego.y + juego.celda *i, juego.celda, juego.celda],1)

    pygame.display.flip()
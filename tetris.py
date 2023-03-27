import pygame

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana y la matriz
cell_size = 20
matrix_width = 10
matrix_height = 20
screen_width = cell_size * matrix_width +100
screen_height = cell_size * matrix_height +100

#Define las piezaS
pieza_o = [[1,1],[1,1]];
pieza_i = [[2,2,2,2]]
pieza_l = [[3,0,0],[3,3,3]]
pieza_j = [[0,0,4],[4,4,4]]
pieza_s = [[0,5,5],[5,5,0]]
pieza_z = [[6,6,0],[0,6,6]]
pieza_t = [[0,7,0],[7,7,7]]

# Crea la ventana
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dibuja la matriz
for row in range(matrix_height):
    for col in range(matrix_width):
        # Calcula las coordenadas de la celda
        x = col * cell_size +50
        y = row * cell_size +50
        # Dibuja el rectángulo de la celda
        pygame.draw.rect(screen, GRAY, (x, y, cell_size, cell_size))
        # Dibuja un borde blanco alrededor de la celda
        pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 1)

# Actualiza la pantalla
pygame.display.update()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

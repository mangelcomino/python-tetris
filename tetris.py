import pygame

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana y la matriz
cell_size = 20
matrix_width = 10
matrix_height = 20
screen_width = cell_size * matrix_width
screen_height = cell_size * matrix_height

# Crea la ventana
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dibuja la matriz
for row in range(matrix_height):
    for col in range(matrix_width):
        # Calcula las coordenadas de la celda
        x = col * cell_size
        y = row * cell_size
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

import pygame
import sys

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
WINDOW_SIZE = [630, 900]
FPS = 60
ROWS = 9
ROW_SIZE = 5
mainClock = pygame.time.Clock()
mainScreen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")


def draw(screen, size):
    screen.fill((255, 255, 255))
    draw_grid(screen, size, ROWS)


def draw_grid(screen, size, ROWS):
    gap = size[0] // ROWS
    for i in range(ROWS + 1):
        pygame.draw.line(screen, (128, 128, 128), (0, i * gap), (size[0], i * gap))
    for i in range(ROWS):
        pygame.draw.line(screen, (128, 128, 128), (i * gap, 0), (i * gap, size[0]))
    for i in range(ROWS // 3 - 1):
        pygame.draw.line(screen, (128, 128, 128), (0, (i + 1) * gap * 3), (size[0], (i + 1) * gap * 3), ROW_SIZE)
    for i in range(ROWS // 3 - 1):
        pygame.draw.line(screen, (128, 128, 128), ((i + 1) * gap * 3, 0), ((i + 1) * gap * 3, size[0]), ROW_SIZE)


# Main game loop ------------------------------------------------------------------------------------------------------#
def main(screen, size, clock):
    run = True
    while run:
        draw(screen, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)


main(mainScreen, WINDOW_SIZE, mainClock)

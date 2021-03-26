import pygame
import sys

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
WINDOW_SIZE = [730, 900]
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
    windowGap = 50
    gap = (size[0] - windowGap * 2) // ROWS
    print(gap)
    for i in range(ROWS + 1):
        pygame.draw.line(screen, (128, 128, 128), (windowGap, i * gap + windowGap),
                         (size[0] - windowGap, i * gap + windowGap), 2)
        pygame.draw.line(screen, (128, 128, 128), (i * gap + windowGap, windowGap),
                         (i * gap + windowGap, size[0] - windowGap), 2)
        if i % 3 == 0:
            pygame.draw.line(screen, (128, 128, 128), (windowGap, i * gap + windowGap),
                             (size[0] - windowGap, i * gap + windowGap), 4)
            pygame.draw.line(screen, (128, 128, 128), (i * gap + windowGap, windowGap),
                             (i * gap + windowGap, size[0] - windowGap), 4)


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

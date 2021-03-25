import pygame
import sys

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
clock = pygame.time.Clock()
WINDOW_SIZE = [800, 1000]
FPS = 60
mainScreen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")

rect = pygame.Rect(100, 100, 100, 100)
speedY = 0


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), rect)


# Main game loop ------------------------------------------------------------------------------------------------------#
def main(screen, size, clock):
    global speedY
    run = True
    while run:
        rect.y += speedY
        speedY += 0.1
        draw(screen)
        if rect.y + rect.height >= WINDOW_SIZE[1]:
            speedY *= -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)


main(mainScreen, WINDOW_SIZE, clock)

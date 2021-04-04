import pygame
import sys
import random
import nodeClass

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
WINDOW_SIZE = [730, 900]
FPS = 60
ROWS = 9
ROW_SIZE = 5
WINDOW_GAP = 50
WINDOW_LENGTH = WINDOW_SIZE[0] - 2 * WINDOW_GAP
mainClock = pygame.time.Clock()
mainScreen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")

# Draw elements
def draw(screen, size, grid):
    screen.fill((255, 255, 255))
    for i in grid:
        for j in i:
            j.draw(screen)
    draw_grid(screen, size, ROWS)

# Draw grid
def draw_grid(screen, size, ROWS):
    gap = (size[0] - WINDOW_GAP * 2) // ROWS
    for i in range(ROWS + 1):
        pygame.draw.line(screen, nodeClass.BLACK, (WINDOW_GAP, i * gap + WINDOW_GAP),
                         (size[0] - WINDOW_GAP, i * gap + WINDOW_GAP), 2)
        pygame.draw.line(screen, nodeClass.BLACK, (i * gap + WINDOW_GAP, WINDOW_GAP),
                         (i * gap + WINDOW_GAP, size[0] - WINDOW_GAP), 2)
        if i % 3 == 0:
            pygame.draw.line(screen, nodeClass.BLACK, (WINDOW_GAP, i * gap + WINDOW_GAP),
                             (size[0] - WINDOW_GAP, i * gap + WINDOW_GAP), 4)
            pygame.draw.line(screen, nodeClass.BLACK, (i * gap + WINDOW_GAP, WINDOW_GAP),
                             (i * gap + WINDOW_GAP, size[0] - WINDOW_GAP), 4)

# Initialize grid with nodes
def make_grid(size):
    grid = []
    gap = (size[0] - WINDOW_GAP * 2) // ROWS
    for i in range(9):
        grid.append([])
        for j in range(9):
            node = nodeClass.Node(i, j, gap, random.randint(1, 9), 50)
            grid[i].append(node)
    return grid

# Translates mouse pos to grid pos
def get_clicked_pos(size):
    x, y = pygame.mouse.get_pos()
    gap = (size[0] - WINDOW_GAP * 2) // ROWS
    row = (x - WINDOW_GAP) // gap
    col = (y - WINDOW_GAP) // gap
    return row, col


# Main game loop ------------------------------------------------------------------------------------------------------#
def main(screen, size, clock):
    # Initialize game loop variables
    run = True
    grid = make_grid(size)

    selected = None

    while run:
        # Draws elements
        draw(screen, size, grid)

        # Event loop
        for event in pygame.event.get():
            # Mouse input (left click)
            if pygame.mouse.get_pressed()[0]:
                # Make selection node
                if WINDOW_GAP <= pygame.mouse.get_pos()[0] <= WINDOW_LENGTH + WINDOW_GAP and WINDOW_GAP <= pygame.mouse.get_pos()[1] <= WINDOW_LENGTH + WINDOW_GAP:
                    row, col = get_clicked_pos(size)
                    spot = grid[row][col]
                    # Reset other nodes
                    if selected:
                        for i in grid:
                            for j in i:
                                j.reset()
                    selected = spot
                    spot.make_selected()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)


main(mainScreen, WINDOW_SIZE, mainClock)

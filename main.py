import pygame
import sys
import requests
import nodeClass

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
WINDOW_SIZE = [1170, 730]
FPS = 60
ROWS = 9
ROW_SIZE = 5
WINDOW_GAP = 50
WINDOW_LENGTH = WINDOW_SIZE[1] - 2 * WINDOW_GAP
mainClock = pygame.time.Clock()
mainScreen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")


# Draw elements
def draw(screen, size, grid, clock):
    screen.fill((255, 255, 255))
    for i in grid:
        for j in i:
            j.draw(screen)
    draw_grid(screen, size, ROWS)
    pygame.display.update()
    clock.tick(FPS)


# Draw grid
def draw_grid(screen, size, ROWS):
    gap = (size[1] - WINDOW_GAP * 2) // ROWS
    for i in range(ROWS + 1):
        pygame.draw.line(screen, nodeClass.BLACK, (WINDOW_GAP, i * gap + WINDOW_GAP),
                         (size[1] - WINDOW_GAP, i * gap + WINDOW_GAP), 2)
        pygame.draw.line(screen, nodeClass.BLACK, (i * gap + WINDOW_GAP, WINDOW_GAP),
                         (i * gap + WINDOW_GAP, size[1] - WINDOW_GAP), 2)
        if i % 3 == 0:
            pygame.draw.line(screen, nodeClass.BLACK, (WINDOW_GAP, i * gap + WINDOW_GAP),
                             (size[1] - WINDOW_GAP, i * gap + WINDOW_GAP), 4)
            pygame.draw.line(screen, nodeClass.BLACK, (i * gap + WINDOW_GAP, WINDOW_GAP),
                             (i * gap + WINDOW_GAP, size[1] - WINDOW_GAP), 4)


# Initialize grid with nodes
def make_grid(size):
    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    values = response.json()['board']
    grid = []
    gap = (size[1] - WINDOW_GAP * 2) // ROWS
    for i in range(9):
        grid.append([])
        for j in range(9):
            node = nodeClass.Node(j, i, gap, values[j][i], 50)
            if node.get_value() != 0:
                node.set_isInitial(True)
            grid[i].append(node)
    return grid


# Translates mouse pos to grid pos
def get_clicked_pos(size):
    x, y = pygame.mouse.get_pos()
    gap = (size[1] - WINDOW_GAP * 2) // ROWS
    row = (y - WINDOW_GAP) // gap
    col = (x - WINDOW_GAP) // gap
    return row, col


# Checks if number in sudoku grid is valid
def check_possible(grid, row, col, number):
    # Check if rows are possible
    for i in range(0, 9):
        if grid[row][i].get_value() == number:
            return False

    # Check if columns are possible
    for i in range(0, 9):
        if grid[i][col].get_value() == number:
            return False

    # Check if squares are possible
    y = (row // 3) * 3
    x = (col // 3) * 3
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if grid[i][j].get_value() == number:
                return False

    return True


# Backtracking algorithm to solve sudoku
def solve(screen, size, grid, clock):
    draw(screen, size, grid, clock)
    # pygame.time.wait(0)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    find = None

    # Finds next empty node
    for row in grid:
        for node in row:
            if node.get_value() == 0:
                find = node

    # Ends algorithm if there are no empty nodes
    if not find:
        return True

    row, col = find.get_pos()

    # Checks All values from 1-9 to see if the values are valid
    for i in range(1, 10):
        if check_possible(grid, row, col, i):

            # Assign value to node
            grid[row][col].set_value(i)
            grid[row][col].set_isUnmodified(True)
            grid[row][col].make_solved()

            # Continues backtracking algorithm
            if solve(screen, size, grid, clock):
                return True

            # If no solutions are left backtrack and find another solution
            grid[row][col].set_value(0)
            grid[row][col].make_error()
            draw(screen, size, grid, clock)

    return False

def input(grid, selected, value):
    if not selected:
        return
    row, col = selected.get_pos()
    if selected:
        if check_possible(grid, row, col, value):
            selected.set_value(value)
            selected.make_input_solved()
        else:
            selected.set_value(value)
            selected.make_input_error()


# Main game loop ------------------------------------------------------------------------------------------------------#
def main(screen, size, clock):
    # Initialize game loop variables
    run = True
    grid = make_grid(size)

    selected = None

    while run:
        # Draws elements
        draw(screen, size, grid, clock)

        # Event loop
        for event in pygame.event.get():
            # Mouse input (left click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    # Make selection node
                    if WINDOW_GAP <= pygame.mouse.get_pos()[0] <= WINDOW_LENGTH + WINDOW_GAP and WINDOW_GAP <= \
                            pygame.mouse.get_pos()[1] <= WINDOW_LENGTH + WINDOW_GAP:
                        row, col = get_clicked_pos(size)
                        spot = grid[row][col]
                        # Reset other nodes
                        if selected:
                            for i in grid:
                                for j in i:
                                    j.make_default()
                        selected = spot
                        spot.make_selected()

            if event.type == pygame.KEYDOWN:

                # Space to solve board
                if event.key == pygame.K_SPACE:
                    for i in grid:
                        for j in i:
                            j.make_default()
                            j.reset_input_color()
                            if not j.get_isInitial():
                                j.set_value(0)
                    solve(screen, size, grid, clock)

                # User input
                if event.key == pygame.K_1:
                    input(grid, selected, 1)
                if event.key == pygame.K_2:
                    input(grid, selected, 2)
                if event.key == pygame.K_3:
                    input(grid, selected, 3)
                if event.key == pygame.K_4:
                    input(grid, selected, 4)
                if event.key == pygame.K_5:
                    input(grid, selected, 5)
                if event.key == pygame.K_6:
                    input(grid, selected, 6)
                if event.key == pygame.K_7:
                    input(grid, selected, 7)
                if event.key == pygame.K_8:
                    input(grid, selected, 8)
                if event.key == pygame.K_9:
                    input(grid, selected, 9)

                if event.key == pygame.K_DELETE:
                    if not selected.get_isInitial():
                        selected.set_value(0)

                if event.key == pygame.K_ESCAPE:
                    grid = make_grid(size)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main(mainScreen, WINDOW_SIZE, mainClock)

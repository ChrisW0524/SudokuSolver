
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

def solve(grid):

    find = None

    for row in grid:
        for node in row:
            if node.get_value() == 0:
                find = node

    if not find:
        return True

    row, col = find.get_pos()

    for i in range(1, 10):
        if check_possible(grid, row, col, i):
            grid[row][col].set_value(i)
            if solve(grid):
                return True
            grid[row][col].set_value(0)

    return False




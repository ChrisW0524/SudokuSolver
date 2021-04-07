import pygame

# Initialize colors (colors control state of cell) --------------------------------------------------------------------#
RED = (255, 0, 0)  # Error
GREEN = (0, 255, 0)  # Solved
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)  # Default
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)  # Selected
TURQUOISE = (64, 244, 208)


class Node:
    def __init__(self, row, col, size, value, offset):
        self.row = row
        self.col = col
        self.size = size
        self.x = row * size + offset
        self.y = col * size + offset
        self.value = value
        self.nodeColor = WHITE
        self.textColor = BLACK
        self.isInitial = False
        self.isUnmodified = False

    def get_pos(self):
        return self.col, self.row

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_isInitial(self):
        return self.isInitial

    def set_isInitial(self, value):
        self.isInitial = value

    def get_isUnmodified(self):
        return self.isUnmodified

    def set_isUnmodified(self, value):
        self.isUnmodified = value

    def draw(self, screen):
        pygame.draw.rect(screen, self.nodeColor, (self.x, self.y, self.size, self.size))
        font = pygame.font.SysFont(None, 60)
        if self.value != 0 or self.isUnmodified:
            screen_text = font.render(str(self.value), True, self.textColor)
            screen.blit(screen_text, (self.x + self.size / 2 - screen_text.get_width() / 2,
                                      self.y + self.size / 2 - screen_text.get_height() / 2))

    def make_default(self):
        self.nodeColor = WHITE

    def make_selected(self):
        self.nodeColor = GREY

    def make_solved(self):
        self.nodeColor = GREEN

    def make_error(self):
        self.nodeColor = RED

    def reset_input_color(self):
        self.textColor = BLACK

    def make_input_error(self):
        self.textColor = RED

    def make_input_solved(self):
        self.textColor = BLUE

import pygame

# Initialize colors (colors control state of cell) --------------------------------------------------------------------#
RED = (255, 0, 0) # Error
GREEN = (0, 255, 0) # Solved
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) # Default
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128) # Selected
TURQUOISE = (64, 244, 208)

class Node:
    def __init__(self, row, col, size, value, offset):
        self.row = row
        self.col = col
        self.size = size
        self.x = row * size + offset
        self.y = col * size + offset
        self.value = value
        self.color = (255, 255, 255)

    def get_pos(self):
        return self.row, self.col

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        font = pygame.font.SysFont(None, 60)
        screen_text = font.render(str(self.value), True, BLACK)
        screen.blit(screen_text, (self.x + self.size / 2 - screen_text.get_width()/2, self.y + self.size / 2  - screen_text.get_height()/2))

    def reset(self):
        self.color = WHITE

    def make_selected(self):
        self.color = GREY

    def make_solved(self):
        self.color = GREEN

    def make_error(self):
        self.color = RED

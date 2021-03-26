import pygame


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
        screen_text = font.render(str(self.value), True, (128, 128, 128))
        screen.blit(screen_text, (self.x + self.size / 2 - screen_text.get_width()/2, self.y + self.size / 2  - screen_text.get_height()/2))

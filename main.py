import pygame
import sys

# Initialize pygame variables -----------------------------------------------------------------------------------------#
pygame.init()
clock = pygame.time.Clock()
WINDOW_SIZE = [800, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku solver")
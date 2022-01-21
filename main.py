import itertools
import pygame
import random


TILE_SIZE = TILE_ROWS, TILE_COLS = 9, 9
MINES = 10
SIZE = WIDTH, HEIGHT = TILE_COLS * 32, TILE_ROWS * 32

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
ORANGE = 255, 140, 0
YELLOW = 255, 255, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 102, 51, 153
MAGENTA = 255, 0, 255


class Tilemap:
    def __init__(self):
        self.tm = [[0 for _ in range(TILE_COLS)] for _ in range(TILE_ROWS)]

    def generate_mines(self):
        for _ in range(MINES):
            while True:
                row = random.randint(0, TILE_ROWS - 1)
                col = random.randint(0, TILE_COLS - 1)
                if self.tm[row][col] == 0:
                    self.tm[row][col] = -1
                    break

    def populate_tiles(self):
        surrounding_mines = {}
        for r, tm_row in enumerate(self.tm):
            for c, tile in enumerate(tm_row):
                if tile == -1:
                    continue

                mines = 0

                if r != 0:
                    if c != 0:
                        surrounding_mines['UL'] = self.tm[r-1][c-1]
                    surrounding_mines['UM'] = self.tm[r-1][c]
                    if c != TILE_COLS - 1:
                        surrounding_mines['UR'] = self.tm[r-1][c+1]
                if r != TILE_ROWS - 1:
                    if c != 0:
                        surrounding_mines['LL'] = self.tm[r+1][c-1]
                    surrounding_mines['LM'] = self.tm[r+1][c]
                    if c != TILE_COLS - 1:
                        surrounding_mines['LR'] = self.tm[r+1][c+1]
                if c != 0:
                    surrounding_mines['ML'] = self.tm[r][c-1]
                if c != TILE_COLS - 1:
                    surrounding_mines['MR'] = self.tm[r][c+1]

                for value in surrounding_mines.values():
                    if value == -1:
                        mines += 1
                self.tm[r][c] = mines
                surrounding_mines.clear()

    def click(self, row, col, *prev):
        tile = self.tm[row][col]
        if tile == -2:
            return False



def pygame_init():
    pygame.init()
    display = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Minesweeper')
    pygame.display.set_icon(pygame.image.load('res/minesweeper_icon.png'))
    return display


def main_loop(display):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill(GREEN)
        pygame.display.flip()


def main():
    tm = Tilemap()
    tm.generate_mines()
    tm.populate_tiles()
    # display = pygame_init()
    # main_loop(display)
    for i in tm.tm:
        for j in i:
            print('%2d' % j, end=' ')
        print()


if __name__ == '__main__':
    main()

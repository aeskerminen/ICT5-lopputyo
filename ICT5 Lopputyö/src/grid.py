from cell import Cell
from random import randint
import pygame


class CellGrid:
    def __init__(self, dimensions, a_color, d_color, sim_speed, surface):
        self.dimensions = dimensions
        self.a_color = a_color
        self.d_color = d_color
        self.sim_speed = sim_speed
        self.surface = surface
        self.run_state = False
        self.cur_generation = 0
        self.cell_size_x = 600 / dimensions[0]
        self.cell_size_y = 600 / dimensions[1]
        self.cells = [[Cell(state=randint(0, 1)) for i in range(dimensions[1])] for j in range(dimensions[0])]

    def generate_next_generation(self):
        if self.run_state:
            self.update_neighbours()
            self.update_population()
            self.cur_generation += 1

    def change_running_state(self):
        self.run_state = not self.run_state

    def generate_new_starting_grid(self):
        self.run_state = False
        self.cur_generation = 0
        self.cells = [[Cell(state=randint(0, 1)) for i in range(self.dimensions[1])] for j in range(self.dimensions[0])]

    def update_population(self):
        w = self.dimensions[0]
        h = self.dimensions[1]
        for x in range(w):
            for y in range(h):
                cur_cell = self.cells[x][y]
                if cur_cell.state == 1:
                    if cur_cell.neighbours > 3 or cur_cell.neighbours < 2:
                        cur_cell.state = 0
                elif cur_cell.state == 0:
                    if cur_cell.neighbours == 3:
                        cur_cell.state = 1

    def count_neighbours(self, x, y):
        n = 0
        w = self.dimensions[0]
        h = self.dimensions[1]
        if x + 1 < w:
            if self.cells[x + 1][y].state == 1:
                n += 1
            if y + 1 < h and x + 1 < w:
                if self.cells[x + 1][y + 1].state == 1:
                    n += 1
            if y - 1 > 0:
                if self.cells[x + 1][y - 1].state == 1:
                    n += 1
        if x - 1 > 0:
            if self.cells[x - 1][y].state == 1:
                n += 1
            if y + 1 < h:
                if self.cells[x - 1][y + 1].state == 1:
                    n += 1
            if y - 1 > 0:
                if self.cells[x - 1][y - 1].state == 1:
                    n += 1
        if y + 1 < h:
            if self.cells[x][y + 1].state == 1:
                n += 1
        if y - 1 > 0:
            if self.cells[x][y - 1].state == 1:
                n += 1
        return n

    def update_neighbours(self):
        w = self.dimensions[0]
        h = self.dimensions[1]
        for x in range(w):
            for y in range(h):
                cur_cell = self.cells[x][y]
                cur_cell.neighbours = self.count_neighbours(x, y)

    def render_grid(self):
        w = self.dimensions[0]
        h = self.dimensions[1]
        for x in range(w):
            for y in range(h):
                # if self.cells[x][y].state == 1:
                rect = pygame.Rect(x * self.cell_size_x, y * self.cell_size_y, self.cell_size_x - 1,
                                   self.cell_size_y - 1)
                pygame.draw.rect(self.surface, self.a_color if self.cells[x][y].state == 1 else self.d_color, rect)

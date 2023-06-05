import math
import random
from random import choice
import pygame
import copy

# Y
ROWS = 20

# X
COLS = 20


# indeksi liste
VISITED = 0
TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4



####################### PYGAME ####################################

RES = WIDTH, HEIGHT = 900, 900
TILE = WIDTH // COLS

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

####################################################################


def createList():
        list = []
        list.append(0)
        list.append(1)
        list.append(1)
        list.append(1)
        list.append(1)
        return list


def checkIndex(list, index):
        if index >= 0 and index < len(list):
                return True
        else:
                return False



def checkCoordiantes(y, x):
     if y >= 0 and y <= ROWS-1 and x >= 0 and x <= COLS-1:
             return True
     else:
             return False

def getIndex(y,x):
        if checkCoordiantes(y,x) == True:
                index = x + y * COLS
                return index
        else:
                return False

def getY(index, totalRows):
        return math.floor(index/totalRows)

def getX(index, totalColums):
        return index%totalColums


def checkVisited(list, y,x):
        if checkCoordiantes(y,x) == True:
                index = getIndex(y,x)
                return list[index][0]
        else:
                return False


def checkNeighbours(list, y, x):
        neighbours = []

        if checkCoordiantes(y,x) == True:
                top = getIndex(y - 1, x)
                right = getIndex(y, x + 1)
                bottom = getIndex(y + 1, x)
                left = getIndex(y, x - 1)

                top_visited = checkVisited(list, y - 1, x)
                right_visited = checkVisited(list, y, x + 1)
                bottom_visited = checkVisited(list, y + 1, x)
                left_visited = checkVisited(list, y, x - 1)

                if not type(top) == bool and not type(top_visited) == bool and top_visited == 0:
                        neighbours.append(top)
                if not type(right) == bool and not type(right_visited) == bool and right_visited == 0:
                        neighbours.append(right)
                if not type(bottom) == bool and not type(bottom_visited) == bool and bottom_visited == 0:
                        neighbours.append(bottom)
                if not type(left) == bool and not type(left_visited) == bool and left_visited == 0:
                        neighbours.append(left)

                if neighbours:
                        return neighbours
                else:
                        return False
        else:
                return False


def choseNeightbour(list, y, x):
        neighbours = checkNeighbours(list, y, x)
        if neighbours:
                return choice(neighbours)
        else:
                return False


def removeWalls(list, current, next):
        dx = getX(current, COLS) - getX(next, COLS)
        if dx == 1:
                list[current][LEFT] = 0
                list[next][RIGHT] = 0
                return list
        elif dx == -1:
                list[current][RIGHT] = 0
                list[next][LEFT] = 0
                return list

        dy = getY(current, ROWS) - getY(next, ROWS)
        if dy == 1:
                list[current][TOP] = 0
                list[next][BOTTOM] = 0
                return list
        elif dy == -1:
                list[current][BOTTOM] = 0
                list[next][TOP] = 0
                return list



def recursiveBacktracker(list, current_cell, stack):
        list[current_cell][VISITED] = 1
        y = getY(current_cell, ROWS)
        x = getX(current_cell, COLS)
        next_cell = choseNeightbour(list,y,x)

        if type(next_cell) == int:
                stack.append(current_cell)
                list2 = removeWalls(list, current_cell, next_cell)
                return recursiveBacktracker(copy.deepcopy(list2), next_cell, copy.deepcopy(stack))
        elif stack:
                current_cell = stack.pop()
                return recursiveBacktracker(copy.deepcopy(list), current_cell, copy.deepcopy(stack))
        else:
                return list


def draw(list):
        for i in range(len(list)):
                x = getX(i, COLS) * TILE
                y = getY(i, ROWS) * TILE

                if list[i][TOP] == 1:
                        pygame.draw.line(sc, pygame.Color('black'), (x, y), (x + TILE, y), 2)
                if list[i][RIGHT] == 1:
                        pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y), (x + TILE, y + TILE), 2)
                if list[i][BOTTOM] == 1:
                        pygame.draw.line(sc, pygame.Color('black'), (x + TILE, y + TILE), (x, y + TILE), 2)
                if list[i][LEFT] == 1:
                        pygame.draw.line(sc, pygame.Color('black'), (x, y + TILE), (x, y), 2)


def main():
        grid = [createList() for row in range(ROWS) for col in range(COLS)]
        stack = []

        #generiranje pocetne tocke
        y = random.randint(0, ROWS)
        x = random.randint(0, COLS)
        start_index = getIndex(y,x)


        maze  = recursiveBacktracker(copy.deepcopy(grid), start_index , copy.deepcopy(stack))

        while True:
                sc.fill(pygame.Color('white'))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                exit()
                draw(maze)

                pygame.display.flip()
                clock.tick(30)


if __name__ == "__main__":
    main()




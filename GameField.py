import random


class GameField:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def spawn_tile(self):
        rnd_x = random.randint(0, self.size - 1)
        rnd_y = random.randint(0, self.size - 1)
        rnd_num = random.randint(0, 10)
        if rnd_num < 7:
            new_number = 2
        else:
            new_number = 4

        if self.grid[rnd_x][rnd_y] == 0:
            self.grid[rnd_x][rnd_y] = new_number

    def _move(self, direction):
        moved = False
        for i in range(self.size):
            if direction in ("left", "right"):
                row = self.grid[i]
            else:
                row = [self.grid[j][i] for j in range(self.size)]

            original_row = row[:]

            row = [val for val in row if val != 0]

            for j in range(len(row) - 1):
                if row[j] == row[j + 1]:
                    row[j] *= 2
                    row[j + 1] = 0

            row = [val for val in row if val != 0]

            if direction in ("right", "down"):
                row = [0] * (self.size - len(row)) + row
            else:
                row = row + [0] * (self.size - len(row))

            if original_row != row:
                moved = True

            if direction in ("left", "right"):
                self.grid[i] = row
            else:
                for j in range(self.size):
                    self.grid[j][i] = row[j]

        return moved

    def move_up(self):
        if self._move("up"):
            self.spawn_tile()

    def move_down(self):
        if self._move("down"):
            self.spawn_tile()

    def move_left(self):
        if self._move("left"):
            self.spawn_tile()

    def move_right(self):
        if self._move("right"):
            self.spawn_tile()

    def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return False
                if j < self.size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
                if i < self.size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False

        return True

    def print(self):
        for row in self.grid:
            print(row)

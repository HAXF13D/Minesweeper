from random import randint, seed


class Sapper:

    def __init__(self, height, width):
        self.__width = width
        self.__height = height
        self.__EMPTY_SIM = '*'
        self.__MINE_SIM = '@'
        self.__HIDE_SIM = '#'
        self.__FLAG_SIM = '%'
        self.__PROBABILITY = 25
        self.__flags = [[isinstance(i + j, int) for j in range(self.__width)] for i in range(self.__height)]
        self.__game_state = True
        self.__generate_field()

    def restart(self, height, width):
        self.__width = width
        self.__height = height
        self.__flags = [[isinstance(i + j, int) for j in range(self.__width)] for i in range(self.__height)]
        self.__game_state = True
        self.__generate_field()

    def in_game(self):
        return self.__game_state

    def __lose(self):
        for i in range(self.__height):
            for j in range(self.__width):
                self.__user_field[i][j] = self.__field[i][j]

    def __check(self):
        if self.__game_state:
            mines_count = 0
            for i in range(self.__height):
                for j in range(self.__width):
                    if self.__field[i][j] == self.__MINE_SIM:
                        mines_count += 1
            open_cell_count = 0
            open_mines_count = 0
            for i in range(self.__height):
                for j in range(self.__width):
                    if self.__field[i][j] != self.__MINE_SIM and self.__user_field[i][j] != self.__HIDE_SIM:
                        open_cell_count += 1
                    if self.__field[i][j] == self.__MINE_SIM and self.__user_field[i][j] == self.__FLAG_SIM:
                        open_mines_count += 1

            if open_cell_count == self.__height * self.__width - mines_count or open_mines_count == mines_count:
                for i in range(self.__height):
                    for j in range(self.__width):
                        self.__user_field[i][j] = self.__field[i][j]
                        if self.__field[i][j] == self.__MINE_SIM:
                            self.__user_field[i][j] = self.__FLAG_SIM
                self.__game_state = False
                print("Вы победили!")
                return True
        return False

    def click(self, x, y, action):
        if 0 <= x < self.__height and 0 <= y < self.__width:
            if action == 'M':
                if self.__user_field[x][y] == self.__FLAG_SIM:
                    self.__user_field[x][y] = self.__HIDE_SIM
                if self.__user_field[x][y] == self.__HIDE_SIM:
                    self.__user_field[x][y] = self.__FLAG_SIM

            if action == 'C':
                if self.__field[x][y] == self.__MINE_SIM:
                    self.__game_state = False
                    self.__lose()
                    print("Вы проиграли!")
                if self.__field[x][y] != self.__MINE_SIM and self.__flags[x][y]:
                    self.__flags[x][y] = False
                    self.__user_field[x][y] = self.__field[x][y]
                    self.__flags[x][y] = False
                    if self.__field[x][y] == '0':
                        self.__open(x + 1, y)
                        self.__open(x - 1, y)
                        self.__open(x + 1, y + 1)
                        self.__open(x + 1, y - 1)
                        self.__open(x - 1, y + 1)
                        self.__open(x - 1, y - 1)
                        self.__open(x, y + 1)
                        self.__open(x, y - 1)
        self.__check()

    def print_field(self):
        for i in range(self.__height):
            print(self.__user_field[i])

    def get_field(self):
        return self.__field

    def __open(self, x, y):
        if 0 <= x < self.__height and 0 <= y < self.__width:
            if self.__field[x][y] != self.__MINE_SIM and self.__flags[x][y]:
                self.__flags[x][y] = False
                self.__user_field[x][y] = self.__field[x][y]
                if self.__field[x][y] == '0':
                    self.__open(x + 1, y)
                    self.__open(x - 1, y)
                    self.__open(x + 1, y + 1)
                    self.__open(x + 1, y - 1)
                    self.__open(x - 1, y + 1)
                    self.__open(x - 1, y - 1)
                    self.__open(x, y + 1)
                    self.__open(x, y - 1)

    def __generate_field(self):
        self.__field = []
        self.__user_field = []
        for i in range(self.__height):
            temp_field = []
            hide_field = []
            for j in range(self.__width):
                temp_field.append(self.__EMPTY_SIM)
                hide_field.append(self.__HIDE_SIM)
            self.__user_field.append(hide_field)
            self.__field.append(temp_field)
        self.__generate_mines()
        self.__put_digits()

    def __generate_mines(self):
        seed()
        for i in range(self.__height):
            for j in range(self.__width):
                choose = randint(1, 100)
                if choose < self.__PROBABILITY:
                    self.__field[i][j] = self.__MINE_SIM

    def __put_digits(self):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__field[i][j] == self.__EMPTY_SIM:
                    self.__put_digit(i, j)

    def __put_digit(self, i, j):
        count = 0
        if i - 1 >= 0:
            if self.__field[i - 1][j] == self.__MINE_SIM:
                count += 1
        if i + 1 < self.__height:
            if self.__field[i + 1][j] == self.__MINE_SIM:
                count += 1
        if j - 1 >= 0:
            if self.__field[i][j - 1] == self.__MINE_SIM:
                count += 1
        if j + 1 < self.__height:
            if self.__field[i][j + 1] == self.__MINE_SIM:
                count += 1

        if i - 1 >= 0 and j - 1 >= 0:
            if self.__field[i - 1][j - 1] == self.__MINE_SIM:
                count += 1
        if i + 1 < self.__height and j - 1 >= 0:
            if self.__field[i + 1][j - 1] == self.__MINE_SIM:
                count += 1
        if j + 1 < self.__height and i - 1 >= 0:
            if self.__field[i - 1][j + 1] == self.__MINE_SIM:
                count += 1
        if j + 1 < self.__height and i + 1 < self.__height:
            if self.__field[i + 1][j + 1] == self.__MINE_SIM:
                count += 1
        self.__field[i][j] = str(count)

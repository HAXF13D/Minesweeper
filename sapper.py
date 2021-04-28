from random import randint, seed


class Sapper:
    __EMPTY_SIM__ = '*'
    __MINE_SIM__ = '@'
    __HIDE_SIM__ = '#'

    def __init__(self, height, width):
        self.__width__ = width
        self.__height__ = height
        self.__GenerateField__()

    def PrintField(self):
        for i in range(self.__height__):
            print(self.__field__[i])

    def GetField(self):
        return self.__field__

    def __GenerateField__(self):
        self.__field__ = []
        for i in range(self.__height__):
            temp_field = []
            for j in range(self.__width__):
                temp_field.append(self.__EMPTY_SIM__)
            self.__field__.append(temp_field)
        self.__GenerateMines__()
        self.__PutDigits__()

    def __GenerateMines__(self):
        seed()
        for i in range(self.__height__):
            for j in range(self.__width__):
                choose = randint(1, 100)
                if choose < 20:
                    self.__field__[i][j] = self.__MINE_SIM__

    def __PutDigits__(self):
        for i in range(self.__height__):
            for j in range(self.__width__):
                if self.__field__[i][j] == self.__EMPTY_SIM__:
                    self.__PutDigit__(i, j)

    def __PutDigit__(self, i, j):
        count = 0
        if i - 1 >= 0:
            if self.__field__[i - 1][j] == self.__MINE_SIM__:
                count += 1
        if i + 1 < self.__height__:
            if self.__field__[i + 1][j] == self.__MINE_SIM__:
                count += 1
        if j - 1 >= 0:
            if self.__field__[i][j - 1] == self.__MINE_SIM__:
                count += 1
        if j + 1 < self.__height__:
            if self.__field__[i][j + 1] == self.__MINE_SIM__:
                count += 1

        if i - 1 >= 0 and j - 1 >= 0:
            if self.__field__[i - 1][j - 1] == self.__MINE_SIM__:
                count += 1
        if i + 1 < self.__height__ and j - 1 >= 0:
            if self.__field__[i + 1][j - 1] == self.__MINE_SIM__:
                count += 1
        if j + 1 < self.__height__ and i - 1 >= 0:
            if self.__field__[i - 1][j + 1] == self.__MINE_SIM__:
                count += 1
        if j + 1 < self.__height__ and i + 1 < self.__height__:
            if self.__field__[i + 1][j + 1] == self.__MINE_SIM__:
                count += 1
        self.__field__[i][j] = str(count)


game = Sapper(10, 10)
game.PrintField()
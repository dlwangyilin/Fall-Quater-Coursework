class HI:
    def __init__(self):
        self.__lst = [65,66,67,68]
    def print(self):
        print(chr(self.__lst[0] + 3))

a = HI()
a.print()
b = 0
print(chr(b))

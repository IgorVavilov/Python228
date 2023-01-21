class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self):
        return f"{self.w}, {self.h}"

    def get_perimetr(self):
        return 2 * (self.w + self.h)

__author__ = 'Igor'

if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__}).')
    r1 = Rectangle(30, 40)
    r2 = Rectangle(20, 50)
    print('r1', r1)
    print('r2', r2)
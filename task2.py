class NumError(Exception):
    def __init__(self, exp, mes):
        self.exp = exp
        self.mes = mes


class Dr:
    def __init__(self, top, bottom):
        if top > bottom:
            raise NumError(top, 'Should')
        self.top = top
        self.bottom = bottom

    def __add__(self, other):
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bot = self.bottom * other.bottom
        return Dr(new_top, new_bot)

    def __sub__(self, other):
        new_top = self.top * other.bottom - other.top * self.bottom
        new_bot = self.bottom * other.bottom
        return Dr(new_top, new_bot)

    def __mul__(self, other):
        if isinstance(other, int):
            new_top = self.top * other
            return Dr(new_top, self.bottom)
        else:
            new_top = self.top * other.top
            new_bot = self.bottom * other.bottom
            return Dr(new_top, new_bot)

    def __eq__(self, other):
        new_num = self.top / self.bottom
        new_num2 = other.top / other.bottom
        return new_num == new_num2

    def __str__(self):
        return f'{self.top} / {self.bottom}'


dr1 = Dr(1, 4)
dr2 = Dr(5, 6)

print(Dr.__add__(dr1, dr2))
print(Dr.__sub__(dr1, dr2))
print(Dr.__mul__(dr1, dr2))
print(Dr.__eq__(dr1, dr2))

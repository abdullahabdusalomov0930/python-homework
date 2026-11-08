# t = Tortburchak(4, 5)
# print(t.yuza())        # 20
# print(t.perimetr())    # 18

class Tortburchak:
    def __init__(self, uzunlik, enlik):
        self.uzunlik = uzunlik
        self.enlik = enlik

    def yuza(self):
        return self.uzunlik * self.enlik

    def perimetr(self):
        return 2 * (self.uzunlik + self.enlik)

t = Tortburchak(4, 5)
print(t.yuza())        # 20
print(t.perimetr())    # 18


# k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
# print(k)
# O'tkan kunlar - Abdulla Qodiriy (1926)

class Kitob:
    def __init__(self, nom, yozuvchi, yil):
        self.nom = nom
        self.yozuvchi = yozuvchi
        self.yil = yil
    def __str__(self):
        return f'{self.nom} - {self.yozuvchi} ({self.yil})'


k = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
print(k)
# O'tkan kunlar - Abdulla Qodiriy (1926)



class Vektor2D:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vektor({self.a}, {self.b})'

    def __add__(self, other):
        return Vektor2D(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vektor2D(self.a - other.a, self.b - other.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


v1 = Vektor2D(3, 5)
v2 = Vektor2D(1, 2)
print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 == v2)
print(v1 == Vektor2D(3, 5))


class Baholar:
    def __init__(self, *baholar):
        self.baholar = baholar
    def __str__(self):
        return f'Baholar{self.baholar}'
    def __len__(self):
        return len(self.baholar)
    def ortacha(self):
        return sum(self.baholar) / len(self.baholar)


b = Baholar(5, 4, 3, 5)
print(b)            # Baholar(5, 4, 3, 5)
print(len(b))       # 4
print(b.ortacha())  # 4.25
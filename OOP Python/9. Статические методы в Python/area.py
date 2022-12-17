from math import pi

class Cylinder:

    def __init__(self, dia, hi):
        self._dia = dia
        self._h = hi
        self.__area = self.make_area(self._dia, self._h)

    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    @property
    def area(self):
        return self.__area

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self,value):
        self._dia=value;
        self.__area = self.make_area(self._dia,self._h)

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self,value):
        self._h=value;
        self.__area=self.make_area(self._dia,self._h)



a = Cylinder(1, 2)
print(a.area)
a.dia=2
print(a.area)
a.h=3
print(a.area)

class Point:
    def __init__(self, x=0, y=0):
        self.valor1 = x
        self.valor2 = y

    def setx(self, x):
        self.valor1 = x

    def sety(self, y):
        self.valor2 = y

    def get(self):
        return print(self.valor1, self.valor2)

    def move(self, offsetx, offsety):
        self.valor1 += offsetx
        self.valor2 += offsety

objeto1 = Point()
objeto2 = Point()

objeto1.setx(2)
objeto1.sety(4)
objeto2.setx(6)
objeto2.sety(8)
print(objeto1.valor1, objeto1.valor2, " - ", objeto2.valor1, objeto2.valor2)

objeto1.move(2,2)
print(objeto1.valor1, objeto1.valor2, " - ", objeto2.valor1, objeto2.valor2)

objeto1.get()

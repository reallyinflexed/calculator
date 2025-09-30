class Calc():
    def __init__(self, n1, n2):   #Инициализируем переменные-значения
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2   #Добавляем действие сложение

    def subtract(self):
        return self.n1 - self.n2   #Добавляем действие вычитание

    def multiply(self):
        return self.n1 * self.n2   #Добавляем действие умножение

    def divide(self):
        if self.n2 == 0:   #Обрабатываем ошибку деления на ноль
            raise ValueError('Делить на ноль нельзя')
        return self.n1 / self.n2   #Добавляем действие деление

c = Calc(78, 10)  #Вносим значения

print(c.divide())  #Выбиреам действие и получаем результат
print(c.multiply())
print(c.subtract())
print(c.add())
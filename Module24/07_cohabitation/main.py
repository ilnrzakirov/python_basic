import random

class People:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        if isinstance(house, House):
            self.house = house
        self.alive = True

    def eats(self):
        if self.house.food >= 20:
            self.satiety += 20
            self.house.food -= 20
            print("{} решил подкрепиться".format(self.name))
        else:
            print("Недостаточно еды в холодильнике, надо поработать")

    def work(self):
        if self.satiety >= 20:
            self.satiety -= 20
            self.house.money += 20
            print("{} немного поработал".format(self.name))
        elif self.satiety == 0:
            self.alive = False
        else:
            print("Нужно поесть")

    def play(self):
        if self.satiety >= 20:
            self.satiety -= 20
            print("{} решил поиграть".format(self.name))
        elif self.satiety == 0:
            self.alive = False
        else:
            print("Нужно поесть")

    def shop(self):
        if self.house.money >= 20:
            self.house.food += 20
            print("{} сходил за едой".format(self.name))
        else:
            print("Недостаточно денег для покупок")



class House:

    def __init__(self):
        self.food = 50
        self.money = 0

house = House()
Tom = People("Tom", house)
Vany = People("Vany", house)

for day in range(365):
    number = random.randint(1, 6)
    if Tom.satiety < 20:
        Tom.eats()
    elif Vany.satiety < 20:
        Vany.eats()
    elif house.food < 20:
        Tom.shop()
        Vany.shop()
    elif house.money < 50:
        Tom.work()
        Vany.work()
    elif number == 1:
        Tom.work()
        Vany.work()
    elif number == 2:
        Tom.eats()
        Vany.eats()
    elif number > 2:
        Tom.play()
        Vany.play()
    if Tom.alive == False:
        print("{} умер".format(Tom))
    elif Vany.alive == False:
        print("{} умерл".format(Vany))
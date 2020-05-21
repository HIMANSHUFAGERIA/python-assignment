class ubber:
    def __init__(self, car):
        self.car = car

    def Innova(self):
        self.rate = 12
        return self.rate

    def Jeep(self):
        self.rate = 12
        return self.rate

    def Swift(self):
        self.rate = 10
        return self.rate

    def Indica(self):
        self.rate = 10
        return self.rate

    def Alto(self):
        self.rate = 10
        return self.rate

class distance (ubber):
    def __init__(self, car, km):
        ubber.__init__ (self, car)
        self.km = km

    def getdistance(self):
        return self.km


class fare (distance):
    def __init__(self, car, km):
        distance.__init__ (self, car, km)

    def price(self):
        if self.car == 1:
            price = self.km * ubber.Innova(self)
            print ("Total fare is Rs. ", price)
        elif self.car == 2:
            price = self.km * ubber.Jeep (self)
            print ("Total fare is Rs. ", price)
        elif self.car == 3:
            price = self.km * ubber.Swift(self)
            print ("Total fare is Rs. ", price)
        elif self.car == 4:
            price = self.km * ubber.Indica (self)
            print ("Total fare is Rs. ", price)
        elif self.car == 5:
            price = self.km * ubber.Alto (self)
            print ("Total fare is Rs. ", price)


car = int(input('Select car\n' \
                 '1. Innova fare 12rs/km\n' \
                 '2. Jeep fare 12rs/km\n' \
                 '3. Swift fare 10rs/km\n' \
                 '4. Indica fare 10rs/km\n '\
                ' 5. Alto fare 10rs/km\n'))

dist = int (input("Enter distance in kilometer: "))
cab = fare (car, dist)
cab.price()
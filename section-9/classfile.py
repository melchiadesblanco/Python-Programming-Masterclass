


class Kettle(object):

    # similar to Java Static Attributes
    power_source = 'eletric'

    def __init__(self, make, price):
        #Attributes
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on =  True

    def switch_off(self):
        self.on = False


A = Kettle('Kenwood', 8.99)
B = Kettle('Hamilton', 14.50)
Kettle.power_source = 'gas'

print(A.make, A.price, A.on, A.power_source)
print(B.make, B.price, B.on, B.power_source)
A.__dict__
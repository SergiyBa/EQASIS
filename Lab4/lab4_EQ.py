import pandas as pd


class Delivery:

    _1kmcost= 0

    def get_cost(self, distance):
        return self._1kmcost*distance

    def set_cost(self, value):
        self._1kmcost= value


class Samovyvoz(Delivery):

    def __init__(self):
        self._1kmcost=0


class Inner(Delivery):

    def __init__(self, cost):

        self.set_cost(cost)


class Outer(Delivery):

    def __init__(self, cost):
        self.set_cost(cost)


class Dodatok:

    def __init__(self):

        self.delivery=pd.Series(['Samovyvoz','Inner','Outer'])
        self.delivery['Samovyvoz'] = Samovyvoz()
        self.delivery ['Inner']= Inner(10)
        self.delivery ['Outer']= Outer(20)


    def calculate_delivery(self, distance, metod):

        return self.delivery[metod].get_cost(distance)


#main

dod=Dodatok()
metod= "Inner"
rasst=15
print(metod, rasst,'km Total cost:', dod.calculate_delivery(rasst, metod))
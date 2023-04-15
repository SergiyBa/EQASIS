import pandas as pd

class Iterator:
    pass


class Cities :

    def __init__(self, table : pd.DataFrame):
        self.cities_list = pd.DataFrame(table)

    def __getitem__(self, item):
        return self.cities_list[item][1]  #повертає якісь обрани властівості, в даному випадку наприклад другу колонку

    def __len__(self):
        return self.cities_list.shape[0]

    def get_recomended_list(self, method: Iterator):
        return self.cities_list.iloc[method.get_list(self)][0]


class Iterator:

    def __init__(self, type, *args):
        self.type = type  # тип функції
        self.param = args  # параметри

    def get_list(self, list: Cities):
        l1=[]

        for i in range(0,len(list)):
            if self.type(list[i], self.param):
                l1.append(i)

        return l1

# функції для визначення приналежности до списка

def type1 (*args):
    if args[0]: # something concrete
        return True
    else:
        return False

def type2 (*args):
    if args[0]: # something concrete
        return True
    else:
        return False

def type3 (*args):
    if args[0]: #  something concrete
        return True
    else:
        return False

# main

nav_list= Iterator(type1, 100)
guide_list= Iterator(type2,['Kharkiv','Lviv'])
own_list= Iterator (type3, "Список.txt")

Ukraine_cities= Cities([['Kiev',12], ['Kharkiv',10]])

print(Ukraine_cities.get_recomended_list(nav_list))
print(Ukraine_cities.get_recomended_list(guide_list))
print(Ukraine_cities.get_recomended_list(own_list))

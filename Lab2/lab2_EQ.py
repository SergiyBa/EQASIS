import pandas as pd

COL=['id', 'address', 'date', 'time', 'phone','name', 'name2', 'type']  #усі текстові  поля
COL_start= ['id', 'address', 'date', 'phone','name', 'type']            # початкові поля
CHECKS =['No delivery','Other person']                  # чекбокси
DATATIME= {1: 1015, 2: 1114, 10: 1118}                # якій час доступен у якої дати наприклад 1го - с 10 до 15 и т.д

class CheckBoxes:

    def __init__(self, names):

        self.isactive = pd.Series(index= names, dtype= bool, data=False)


    def activate(self, name):

        self.isactive[name] = True

    def deactivate(self, name):

        self.isactive[name] = False

class TextBoxes:

    def __init__(self, names, data):
        self.visible = pd.Series(index= names, dtype= bool, data=False)
        self.data = data

    def show(self, name):
       self.visible[name] = True

    def kill(self, name):
       self.visible[name] = False

    def set(self, name, data):
        self.data [name] = data

class Mediator:

    def __init__(self, data):

        self.checkboxes = CheckBoxes(CHECKS)

        self.textboxes= TextBoxes (COL, data)

        # відображення текстових полей в начале

        for i in COL_start:
            self.textboxes.visible[i]=True

    def check (self, name):

        self.checkboxes.activate(name)

        if name == 'Other person' :
            self.textboxes.show(['name2','phone'])

        if name == 'No delivery':
            self.textboxes.kill(['address','date', 'time','name2'])

    def uncheck (self, name):

        self.checkboxes.deactivate(name)

        if name == 'Other person':
            self.textboxes.kill(['name2'])

        if name == 'No delivery':
            self.textboxes.show(['address','date', 'time'])

    def date_time(self, date):

        self.textboxes.set('time', DATATIME[date])


class Zamovnik:

    def __init__(self, fields):
        self.data = pd.Series(index=fields, dtype= str)

#main

zamovnik1 = Zamovnik(COL)

mediator1 = Mediator(zamovnik1)











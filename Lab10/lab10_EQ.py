
class HtmlForm:
    _title = ''
    _data = None

    def __init__(self, title):
        self._title = title

    def set(self, *args):
        self._data = args

    def get(self):
        return self._data

    def show(self):
        print(self._title, self._data)


class SelectForm(HtmlForm):

    def __init__(self, title, items=[]):
        super().__init__(title)
        self._data = items


class InputForm(HtmlForm):

    def __init__(self, title, type):
        super().__init__(title)
        self._data = type(input('Enter ' + self._title + ' '))


class Fieldset(HtmlForm):

    def __init__(self, title, *args):
        super().__init__(title)
        self._data = list(args)

    def add(self, element: HtmlForm):
        self._data.append(element)

    def show(self):
        print(self._title)
        for i in self._data:
            i.show()

#main

s1= SelectForm('Color', ['Red', 'Blue', 'Green'])

i1= InputForm('Name', str)
i2= InputForm('Age', int)

f1= Fieldset('Person', i1, i2)
f1.add(SelectForm('Country', ['Usa', 'Ukraine', 'Brazil']))
f1.show()

f2 = Fieldset('Person+color', f1, s1, Fieldset('Some other fields',InputForm('New data', float)))
f2.show()









class Worker:
    __title=''
    __salary=0
    def __init__(self, title , salary):
        self.__title=title
        self.__salary=salary

    def get_salary(self):
        return self.__salary


class Department:
    def __init__(self, workers):
        self.__workers=workers

    def get_workers(self):
        return self.__workers


class Company:
    def __init__(self, departments):
        self.__departments=departments

    def get_departments(self):
        return self.__departments


class Report:
    def get_report(self, type, obj):
        if type == 'salary':
            if isinstance(obj, Worker):
                return obj.get_salary()

            if isinstance(obj, Department):
               return self.get_dep_report(type,obj)

            if isinstance(obj, Company):
                return self.get_company_report(type,obj)

    def get_dep_report(self, type, obj):
        if type == 'salary':
            total = 0
            for i in obj.get_workers():
                total += i.get_salary()
            return total

    def get_company_report(self, type, obj):
        if type == 'salary':
            total = 0
            for i in obj.get_departments():
                total += self.get_dep_report(type, i)
            return total


#main

Ivan=Worker("помічник", 1500)
Petro=Worker("Головний бухгалтер", 2500)
Slava=Worker("Менеджер", 2000)
Tanya=Worker("Менеджер", 3000)

Buhgalteria = Department([Ivan,Petro])
Sales = Department([Slava,Tanya])

OurCompany = Company([Buhgalteria,Sales])

r1= Report().get_report('salary', Buhgalteria)
r2= Report().get_report('salary', OurCompany)
r3= Report().get_report('salary', Tanya)

print(r1, r2, r3)

class Singleton:

    __inst = None
    __param = None

    def __init__(self, *args, **kwargs):
        self.__param=args[0]

    def __new__(cls, *args, **kwargs):
        if cls.__inst == None:
            cls.__inst=super().__new__(cls)

        return cls.__inst

class DB_MongoDB(Singleton):

    def query (q:str):
        # some action
        answ = True
        return answ


class DB_PostgreSQL(Singleton):

    def query(q: str):
        # some action
        answ = True
        return answ

#main

db1=DB_MongoDB("qqq.txt")
db2=DB_MongoDB("qqq.txt")

db3=DB_PostgreSQL("rrr.txt")
db4=DB_PostgreSQL("rrrr.txt")

print(db1, db2, db3, db4)
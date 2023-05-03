
class QueryBuilder:
    def __init__(self):
        self._query=''

    def reset(self):
        self._query=''

    def select(self):
        pass

    def where(self):
        pass

    def limit(self):
        pass

    def _is_complete(self):
        return bool (self._query)

    def getSQL(self):
        if self._is_complete():
            return self._query
        else:
            return None

class PostgreQueryBuilder (QueryBuilder):

    def select(self, param):
        self._query += ' select '+ str(param)

    def where(self, param):
        self._query += ' where '+ str(param)

    def limit(self, param):
        self._query += ' limit '+ str(param)


class MyQueryBuilder (QueryBuilder):

    def select(self, param):
        self._query += ' select from '+ str(param)

    def where(self, param):
        self._query = ' * where '+ str(param) + self._query

    def limit(self, param):
        self._query += ' to limit '+ str(param)

class Database:

    def __init__(self, builder: QueryBuilder):
       self.qb = builder

#main

db= Database(MyQueryBuilder())
db.qb.limit(3)
db.qb.where(1)
print(db.qb.getSQL())

db= Database(PostgreQueryBuilder())
db.qb.limit(10)
db.qb.where(1)
print(db.qb.getSQL())





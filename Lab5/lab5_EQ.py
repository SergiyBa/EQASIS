from datashape import json

class ApiObject:
    _data= object

    def __init__(self, data):
        self._data= data

    def get(self):
        return self._data

    def save_data(self, data):
        try:
            self._data = data
            return True

        except Exception:
            return False

    def validate(self, data):
        return bool(data)

    def hook(self):
        pass


class User(ApiObject):

    def __init__(self, data, email):
        super().__init__((data, email))


    def save_data(self, data):
        del data.email
        return super().save_data(data)


class Order(ApiObject):

    def save_data(self, data):
        return super().save_data(), json(data)


class Item(ApiObject):

    def validate(self, data):
        val= super().validate(data)
        if not val:
            print("Товар не пройшов валидацію")
        return val


class Api:
    orders=[ApiObject(None)]
    items=[ApiObject(None)]
    users=[ApiObject(None)]

    def create_order(self, data):
        self.orders.append(Order(data))

    def create_item(self, data):
        self.items.append(Item(data))

    def create_user(self, data, email):
        self.users.append(User(data,email))

    def get_obj(self, obj: ApiObject):
        return obj.get()

    def validate(self, obj:ApiObject, data):
        return obj.validate(data)

    def save(self, obj: ApiObject, data):
        if obj.validate(data):
            return obj.save_data(data)
        else:
            print("Data can't be saved")
            return False

    def use_hook(self, obj:ApiObject):
        obj.hook()


#main

a=Api()

a.create_user("Johh", "aa@ddd.com")
a.create_item("tovar")
a.create_order("order1")

a.save(a.users[0],"john1")

print (a.validate(a.orders[0],"order"))

a.use_hook(a.orders[0])

a.save(a.orders[0],"order")


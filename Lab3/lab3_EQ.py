
class Saver:

    def __init__(self):

        self.__stack = []

    def can_cancel(self):  #TRUE - можливо відминити, False - ні

        if len(self.__stack) == 0 :
            return False

        else:
            return True

    def do_restore(self):

        if self.can_cancel():

            return self.__stack.pop()

        else:

            return None

    def do_save(self, cond):

        self.__stack.append(cond)



class User :

    def __init__(self, data):

        self.__snaphots= Saver()
        self.__settings=[]
        self.__data= data


    def save(self):

        self.__snaphots.do_save(self.__settings)


    def undo(self):

        self.__settings= self.__snaphots.do_restore()


    def edit(self):

        self.save()

        #do something




# main

u1=User([1,2,3,4])

u1.edit()

u1.undo()



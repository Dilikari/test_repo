# сделать функция которая будет два числа от а и б


class DataManager:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dict_generation(self):
        dict1 = {}
        for x in range(self.a, self.b):
            dict1[x] = "hello"

        print(dict1)




    def list_generation(self):
        lst = []
        for x in range(self.a, self.b):

            lst.append(x)
        print(lst)

t =DataManager(1, 10)
t.dict_generation()







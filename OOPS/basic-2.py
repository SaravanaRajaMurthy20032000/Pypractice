# import calendar
# year = 2023
# m = 5
# result = calendar.month(year,m)
# print(result)

"""INHERITANCE"""
# base class
class animal:
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")
# derived class
class dog(animal):
    def friend(self):
        print("I'm Human's best friend")
    
dog1 = dog()
dog1.eat()
dog1.sleep()
dog1.friend()
# 
"""ENCAPSULATION"""
class computer:
    def __init__(self):
        self.__maxprice = 800
""" Basics of function """
def deco(func):
    def intro():
        print("Hai")
        func()
        print("Welcome to my Home")
    return intro
# @deco
def greet():
    print("Hello")
    
greet = deco(greet)
print(greet.__name__)

# 
""" Function as a Parameter """
def fun1():
    print('this is function-1')
def fun2(ref):
    ref()
    print('this is function-2')
    
fun2(fun1)
# 
"""  """
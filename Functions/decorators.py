        # DECORATORS
# A decorator is a function that takes another function 
# and extends the behavior of the latter function without explicitly modifying it.

def fun(ref):
    def process():
        data = ref()
        return data.upper()
    return process

def myfunc():
    return "Welcome home"

res = fun(myfunc)
print(res()) #changed the answer, but the original is not changed that answer is below.

print(myfunc()) # this is the original.

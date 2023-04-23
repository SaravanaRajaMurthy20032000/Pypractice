# table creating
# def table(n,t):
#     if n != 0:
#         table(n-1,t)
#         print(n,'*',t,"=",n * t)
    
# n = int(input("enter the num: "))
# t = int(input("enter the table: "))
# table(n,t)

# factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("enter the num: "))
res = fact(n)
print(res)

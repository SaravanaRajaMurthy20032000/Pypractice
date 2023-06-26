# class oops:
#     def fun1(self,name,age):
#         self.new = name 
#         self.new2 = age

#     def fun2(self):
#         return f"name and age is {self.new},{self.new2}"

# obj = oops()
# obj.fun1('saravana',25)
# print(obj.fun2())


from datetime import date 
class Student:
    def __init__(self,name,dob,city):
        self.name = name
        self.dob = dob
        self.city = city
    
    def address(self):
        add = f"name: {self.name}\nage: {self.dob}\
                \nCity: {self.city}"
        return add
    
    def age(self):
        current_year = date.today().year
        return current_year - self.dob

stu1 = Student('Saravana',2000,'Madras')
stu2 = Student('Raja',1999,'Erode')
print(stu1.age()) ; print(stu1.address())
print(stu2.age()) ; print(stu2.address())


# class car:
#     def __init__(self,license_plate,model,color):
#         self.license_plate = license_plate
#         self.model = model
#         self.color = color

#     def slots(self,cars,slot):
#         self.cars_added = cars
#         self.slot = slot
    
# p1 = car("TS04 bl 0954","Renault","white")
# p1.slots(4,10)

# print(p1.model)
# print(p1.slot)

# 

# class retail:
#     pass

# p1 = retail()
# p2 = retail()
# print(p1); print(p2)

# class retail:
#     def __init__(self,name,price,discount):
#         self.name = name
#         self.price = price
#         self.discount = discount

# p1 = retail('chandru',1233,.04)
# p2 = retail('raju',3454,.07)

# print(p1.discount)
# print(p2.name)
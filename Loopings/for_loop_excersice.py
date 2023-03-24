#  1s FOR LOOP QUESTION
name = input("enter the name: ")
c = int(input("how many times to add: "))
for i in range(c):
    print(name)

# 2nd  FOR LOOP QUESTION
name = input("user value: ")
res = []
for i in range(len(name)):
    if name[i] == 'a':
        res.append(i)
        print(res)
if res != 'a':
    print("none")
else:
    print(f"\'a\' is in the variable are {res}")

# 3rd
name = input("Enter your name: ")
for i in range(len(name) + 1):
    print(name[0:i])

# 4th 
name = input("enter your name: ")
cap = ""
for i in range(len(name)):
    if i % 2 == 0:
        cap += name[i].lower()
    else:
        cap += name[i].upper()
print(cap)
# 5th
for i in range(1,21):
    print(i,i ** 2)
# 6th 
text = input("enter the text: ")
c = 0
for space in text:
    if space == ' ':
        c+=1
print(c)
# 7th 
for i in range(8,90,3):
    print(i)
# 8th
for i in range(100,1,-2):
    print(i)
# 9th 
for i in range(10,0,-1):
    print(i)
# 10th
count = 0
for i in range(1, 1001):
    square = i ** 2
    if square % 10 == 4:
        count += 1
print("There are", count, "squares.")
# 11th 
c = 0
c_2 = 0
for i in range(1,1001):
    sqt = i ** 2
    if sqt % 10 == 4:
        c += 1
    elif sqt % 10 == 9:
        c_2 += 1
print("There are", c, "squares.")
print("There are", c_2, "squares.")
# 12th
for i in range(1,1001):
    if i % 7 == 0:
        if i % 10 == 6:
            print(i)
# 13th
for i in range(1,10001):
    if i % 10 == 3:
        print(i)
# 14th 
list = []
for i in range(1,101):
    one = i * '1'
    list.append(one)
    i+=1
print(list)
# 15th
c = 5
for i in range(1, 6):
    print(' ' * c,end='')
    print('* ' * i)
    c -= 1

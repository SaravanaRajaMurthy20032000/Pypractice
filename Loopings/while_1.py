# 
i = 1
while i <= 10:
    if i == 5: 
        print(i)
    i += 1

# 
i = 10
while i <= 20:
    print(i)
    i += 1

# 
i = 20
while i >= 10:
    print(i)
    i -= 1

# 
i = -30
while i <= 0:
    print(i)
    i += 1

# 
i = -10
while i <= 10:
    print(i)
    i += 1

# 
i = -30
while i >= -40:
    print(i)
    i -= 1

# 
i = 20
while i <= 40:
    print(i)
    i += 1

# 
i = 1
while i <= 100:
    if i % 17 == 0: 
        if i % 10 == 5: 
            print(i)
    i += 1

# 
i = 1
while i <= 50:
    if i % 5 == 0:
        if i % 10 == 5:
            print(i)
    i += 1

# 
s = int(input("enter the S: "))
if s >=1 and s <=50:
    i = 1
    while i <= 50:
        if i % 2 == 0:
            # print(i)
            print(f"{i} is EVEN")
        i += 1
elif s >= 51 and s <= 100:
    i = 51
    while i <= 100:
        if i % 2 != 0:
            # print(i)
            print(f"{i} is ODD")
        i += 1
else:
    print("1 to 100")


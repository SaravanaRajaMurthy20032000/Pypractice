d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
for x in d:
    print (x,d[x]) 
# o/p:
    #Orange 40
    # Mango 30
    # Banana 15
    # Peach 20
# KEYS()
d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
print(d.keys()) # o/p: dict_keys(['Orange', 'Mango', 'Banana', 'Peach'])
# VALUES()
d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
print(d.values()) # o/p: dict_values([40, 30, 15, 20])
# ITEMS()
d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
print(d.items()) # o/p: dict_items([('Orange', 40), ('Mango', 30), ('Banana', 15), ('Peach', 20)]) "in list of tuples"

# 
f = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
for fruit, cost in f.items():
    print(fruit, cost)
    
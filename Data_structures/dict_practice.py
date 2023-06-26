# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# for x in d:
#     print (x,d[x]) 
# o/p:
#     #Orange 40
#     # Mango 30
#     # Banana 15
#     # Peach 20
# # KEYS()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.keys()) # o/p: dict_keys(['Orange', 'Mango', 'Banana', 'Peach'])
# # VALUES()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.values()) # o/p: dict_values([40, 30, 15, 20])
# # ITEMS()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.items()) # o/p: dict_items([('Orange', 40), ('Mango', 30), ('Banana', 15), ('Peach', 20)]) "in list of tuples"

# # 
# f = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# for fruit, cost in f.items():
#     print(fruit, cost)
    
# 
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15}
# # d['peach'] = 50
# print(d)

# qm = {}
# qm['emp_id'] = 1071
# qm['Name'] = 'Saravana'
# qm['Age'] = 22
# qm['mail_id'] = 'saravana20@gmail.com'
# qm_2 = {}
# qm_2['emp_id'] = 1008
# qm_2['Name'] = 'Raja'
# qm_2['Age'] = 24
# qm_2['mail_id'] = 'raja24@gmail.com'
# qm_3 = {}
# qm_3['emp_id'] = 1118
# qm_3['Name'] = 'Kumar'
# qm_3['Age'] = 54
# qm_3['mail_id'] = 'kumar54@gmail.com'

# res = []

# for i in qm,qm_2,qm_3:
#     res.append(i)
# print(res)

my_dict = {'name': 'raja', 'age': 24}
new_dict = my_dict.values()
print(new_dict)
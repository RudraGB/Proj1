from collections import OrderedDict
import numpy as np
my_dict = {'banana': 5, 'apple': 2, 'cherry': 8}
# Sorting Using sort()
my_list = list(my_dict.keys())
print(my_list)
my_list.sort()
sorted = {i: my_dict[i] for i in my_list}
print(sorted)

# sorting using sorted()
for i in sorted(my_dict.keys()):
   print(i, end= " ")

my_dict_sorted = OrderedDict(sorted(my_dict.items()))
print(my_dict_sorted)



# Sorting key-value pairs by value, and by key if values are the same
sorted_items = sorted(my_dict.items(), key = lambda kv: (kv[1], kv[0]))
sorted_dict = dict(sorted_items)
print(sorted_dict)


#Sorting Dictionary By Value using Numpy
keys = list(my_dict.keys())
values = list(my_dict.values())
sorted = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted}
print(my_dict)
print(sorted_dict)


#Sorting Dictionary By Value using sorted() method and asc and desc
value_based = {key : value for key, value in sorted(my_dict.items(), key=lambda item: item[1])}
valure_reverse_based = {key : value for key, value in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
print(value_based)
print(valure_reverse_based)

#my_dict = {'apple': '30', 'banana': '20', 'cherry': '10'}
# Sort dictionary by values (strings converted to integers for numeric comparison)
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[0])}
print(sorted_dict)

#adding values
#Input : {‘a’: 100, ‘b’:200, ‘c’:300}
#Output : 600

data = {'a': 100, 'b':200, 'c':300} 
add = list(data.values())
result =  sum(add)
print(f" Addition of values is {result}")

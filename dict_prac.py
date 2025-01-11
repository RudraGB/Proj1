#Input : {‘a’: 100, ‘b’:200, ‘c’:300}
#Output : 600

from operator import itemgetter 

#data = {'a': 100, 'b':200, 'c':300} 
#add = list(data.values())
#result =  sum(add)
#print(f" Addition of values is {result}")

#print(sys.getsizeof(data))

data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

print(sorted(data_list, key = itemgetter("name")))



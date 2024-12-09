def sum_numbers():
    with open('num.txt', 'r') as file:    
        numbers = file.readlines()
        total = 0
        for line in numbers:
            total = int(line) + total
        print (total)

sum_numbers()


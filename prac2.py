def sum_even_numbers():
    with open("num.txt",'r') as file:
        lines = file.readlines()
        total=0
        for line in lines:
            num_list = line.split(',')
            for num in num_list:
                if int(num) % 2 == 0: 
                    total = int(num) + total

        print(total)
            

sum_even_numbers()

           


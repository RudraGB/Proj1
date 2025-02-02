from collections import Counter
def amount_earned(shoe_counter,desired_size,shoe_price):
   
    if desired_size in shoe_counter.key():
       if shoe_counter[desired_size] > 0:
           count = shoe_counter[desired_size]
           count = count - 1
           shoe_counter[desired_size] = count
           return shoe_price
       else:
           return 0
    else:
       return 0  


if __name__ == '__main__':
    X = input() #number of shoes
    available_sizes =list(map(int,input().split(" ")))
    shoe_counter = Counter(available_sizes)
    N = int(input()) #number of customers
    amount = 0
    for _ in range(N):
        desired_size, shoe_price = map(int,input().split(" "))
        amount = amount + amount_earned(shoe_counter,desired_size,shoe_price)
    print(amount)
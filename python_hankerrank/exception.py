T = int(input())
for _ in range(T):
    try:
        a,b = map(int,input().split(" "))
        #division = a // b
        print(a // b)
    except ZeroDivisionError as e:
        print("Cannot divide by 0",e)
    except ValueError as v:
        print("Not appropriate Value",v)

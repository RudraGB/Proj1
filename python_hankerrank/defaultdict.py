from collections import defaultdict

if __name__ == '__main__':
    a_list = []
    b_list = []
    final_list =[]
    n, m = map(int,input().split(" "))
    for _ in range(n):
        a_list.append(input())
    for _ in range(m):
        b_list.append(input())
    
    for letter in b_list:
        if letter in a_list:
            final_list =a_list.index(letter)
            
        else:
           print(-1)

    

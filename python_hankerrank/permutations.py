from itertools import permutations

if __name__ == '__main__':
    s, k = input().split(" ")
    k = int(k)
    comb = sorted(permutations(s,k))
    print(comb)
    for c in comb:
        print("".join(c))
        
    
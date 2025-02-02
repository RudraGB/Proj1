from itertools import product


def cartesian_product(list1, list2):
    result = product(list1,list2)
    return sorted(result)


if __name__== '__main__':
    A = (map(int,input().split(" ")))
    B = (map(int,input().split(" ")))
    product = cartesian_product(A,B)
    print(*product)
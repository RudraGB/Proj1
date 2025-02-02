if __name__ == '__main__':
    N = int(input())
    my_list =[]
    for _ in range(N):
        command, *args = input().split()
        arguments = list(map(int, args))
        if command == "insert":
            my_list.insert(arguments[0],arguments[1])
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(arguments[0])
        elif command == "append":
            my_list.append(arguments[0])
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
            
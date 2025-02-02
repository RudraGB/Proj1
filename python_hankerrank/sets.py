if __name__ == '__main__':
    country_stamp= []
    n = int(input())
    for _ in range(n):
        country_stamp.append(input())
    
    unique_stamps = set(country_stamp)
    total_stamps = len(unique_stamps)
    print(total_stamps)
   
    
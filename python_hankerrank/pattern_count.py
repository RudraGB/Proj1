def count_substring(string, sub_string):
        if sub_string in string:
           counter = counter+1
        return counter
 
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
   
def swap_case(s):
    modified_string=''
    for char in s:
        if (char.islower()):
            modified_string = modified_string + char.upper()
        else:
            modified_string= modified_string + char.lower()
    return modified_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


            
            

            

        

        
           


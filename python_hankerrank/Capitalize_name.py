import os
def solve(s):
    
    f_name, l_name = s.split(" ")
    first_name = f_name[0].upper() + f_name[1::]
    last_name = l_name[0].upper() + l_name[1::]
    modified_name = first_name + " " + last_name
    
    return modified_name
    
    #print(f"{first_name} {last_name}")

      

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    

def mutate_string(string, position, character):
    l = list(string)
    l[position]= character
    m_string = ''.join(l)    
    
    return m_string

if __name__ == '__main__':
    s = input()
    i, c = input().split() # position and character to place
    s_new = mutate_string(s, int(i), c)
    print(s_new)
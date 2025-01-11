def pattern_match(string, pattern):
    i, j = 0,0
    for char in string:
        if char == pattern[j]:
            j=j+1
        if j == len(pattern):
            return True
        i = i+1
    return False

print(pattern_match("rudra", "aj"))

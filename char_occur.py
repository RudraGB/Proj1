#occurence of unique char in a string


sentence = "Hello World"
unique_char = set(sentence)
for char in unique_char:
    occurence = sentence.count(char)
    print(f"{char} occurs :{occurence} times")


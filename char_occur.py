#occurence of unique char in a string


sentence = "Hello World"
unique_char = set(sentence)
for char in unique_char:
    occurence = sentence.count(char)
    print(f"{char} occurs :{occurence} times")

#Input: 
#string = "engineers rock"
#pattern = "er";


def check_pattern(input, pattern):
    if pattern in input:
        print(f"Pattern {pattern} found in {input}")
    else:
        print(f"{pattern} not found in input {input}")

check_pattern("engineers rock","er")

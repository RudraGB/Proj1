#Write a Python program to count the number of vowels in a given string.
#The program should take input from the user and display the count of vowels (a, e, i, o, u, case-insensitive) in the string.

sentence = input("Enter a string")
count=0
for letter in sentence:
    if letter in ['a','e','i','o','u']:
        count+= 1
print(count)








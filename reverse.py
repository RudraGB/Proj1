#Reverse a String
#Write a Python program to reverse a string entered by the user.
#Example: Input: "hello" Output: "olleh"


to_reverse = input("Enter a string to be reversed:  ")
reversed = to_reverse[::-1]
print(f"The reversed string is {reversed}")
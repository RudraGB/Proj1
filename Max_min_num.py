numbers =[56,23,12,10,9]
maxNum = numbers[0]
minNum = numbers[0]

for num in numbers:
    if num > maxNum:
        maxNum = num
    if num < minNum: 
        minNum = num
print(f"Maximum number is {maxNum} and Minimum number is {minNum}")


#largest_number = max(numbers)
#smallest_number = min (numbers)

#print (f"The largest number is {largest_number}")
#print (f"The smallest number is {smallest_number}")


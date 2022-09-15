# Iterate from the start to the end number of the first 10 numbers, and in each iteration print the sum of the current number with the previous number 


# Using the First Method
numbers = [*range(5)]
values = [x for x in range(10)]
start = 0
for number in values:
    sum = start + number 
    print(f"ilteration value: {number}, starting value: {start} and the sum is {sum}")
    start = number 
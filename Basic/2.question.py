# Ilterate from the start number to the end of the first numbers, and in each ilteration print the sum of the current number with the previous number 

# numbers = [*range(5)]
values = [x for x in range(8)]
start = 0
for number in values:
    sum = start + number 
    print(f"ilteration value: {number}, starting value: {start} and the sum is {sum}")
    start = number 
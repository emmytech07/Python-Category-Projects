numbers = [*range(5)]
values = [x for x in range(8)]
start = 0
for number in values:
    sum = start + number 
    print(f"ilteration value: {number}, starting value: {start} and the sum is {sum}")
    start = number 
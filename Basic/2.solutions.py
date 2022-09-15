# Using Function to resolve Question 2.

def sum_Ilteration (numbers):
    initial_value = 0

    for num in range(numbers):
        total = initial_value + num
        print(f"Starting Number: {num}, initial number: {initial_value}, sum of the number {total}")

        initial_value = num
sum_Ilteration(10)
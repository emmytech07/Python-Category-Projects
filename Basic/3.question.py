#display a value at the even indices
#display a character at the even indices

def print_even(num):
    character = "@#$%"
    for x in range(num):
        if x % 2 ==0:
            print (f"Even Number: {x} with chracter: {character }")
        
value = print_even(10)
print(value)
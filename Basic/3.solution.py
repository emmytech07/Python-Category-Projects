#display a character at the even indices

# Solution to question 2

def print_even_index(str):
    for char in range(0, len(str), 2):
        print(f"Index [", char,"]", str[char])

string = "Computer Study"
print_even_index(string)
print_even_index(string)
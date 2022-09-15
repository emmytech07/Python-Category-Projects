# Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string 

# Method 1
Giver_string = "Code Analogy"
n = 4

container = ''
for x in range(0, len(Giver_string)):
    if x <= n:
        container = container +Giver_string[x]
print(container)


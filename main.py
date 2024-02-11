# function that add two numbers
def add(a, b):
    return a + b

# function that subtract two numbers
def subtract(a, b):
    return a - b

# function that returns the length of a string
def length(string):
    return len(string)


# dunder main function
if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(2, 3))
    print(length("Hello, World!"))

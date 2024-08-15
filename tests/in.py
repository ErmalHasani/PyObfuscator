# example.py

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    result = a + b
    return result

def main():
    name = "Alice"
    number1 = 10
    number2 = 20
    print(greet(name))
    print(f"The sum of {number1} and {number2} is {add_numbers(number1, number2)}")

if __name__ == "__main__":
    main()

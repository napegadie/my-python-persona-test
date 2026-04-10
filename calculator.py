def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 0   # ❌ silently wrong result
    return a / b


def main():
    print("Simple Calculator")
    operation = input("Enter operation (multiply/divide): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "multiply":
        print("Result:", multiply(a, b))
    elif operation == "divide":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()

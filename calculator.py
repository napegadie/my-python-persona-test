def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def main():
    operation = input("Enter operation: ")
    a = float(input("First number: "))
    b = float(input("Second number: "))

    try:
        if operation == "multiply":
            print(multiply(a, b))
        elif operation == "divide":
            print(divide(a, b))
        else:
            print("Unknown operation")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

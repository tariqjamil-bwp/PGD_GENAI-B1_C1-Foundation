from argparse import ArgumentParser

def add(x,y):
    return x+y
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def main():
    parser = ArgumentParser(description="Simple Command Line Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operator", choices=['+', '-', '*', '/'], help="Operation: +, -, *, /")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    if args.operator == '+':
        result = add(args.num1, args.num2)
    elif args.operator == '-':
        result = subtract(args.num1, args.num2)
    elif args.operator == '*':
        result = multiply(args.num1, args.num2)
    elif args.operator == '/':
        result = divide(args.num1, args.num2)
    else:
        print("Invalid operator. Please enter +, -, *, /")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
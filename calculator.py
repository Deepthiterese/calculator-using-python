from add import add;
from subtract import subtract;
from multiply import multiply;
from divide import divide;


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation number (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
    else:
     print("Invalid input")
   
if __name__ == "__main__":
    main()
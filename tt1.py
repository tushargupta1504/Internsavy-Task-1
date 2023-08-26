def main():
    print("Welcome to the Simple Calculator App!")

    while True:
        print("\nAvailable operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 5:
            print("Exiting the calculator app.")
            break
        
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            continue
        
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        
        if choice == 1:
            result = first_number + second_number
            print("Result:", result)
        elif choice == 2:
            result = first_number - second_number
            print("Result:", result)
        elif choice == 3:
            result = first_number * second_number
            print("Result:", result)
        elif choice == 4:
            if second_number != 0:
                result = first_number / second_number
                print("Result:", result)
            else:
                print("Cannot divide by zero.")
        
if __name__ == "__main__":
    main()

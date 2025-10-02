def simple_calculator():
    """Perform a simple arithmetic operation based on input."""
    print("Command-Line Calculator")
    
    try:
        # Get the two numbers
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        
        # Get the operation
        operation = input("Enter operation (+, -, *, /): ")
        
        result = None
        
        # Determine which operation to perform
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero!")
                return # Exit the function if division by zero occurs
        else:
            print(f"Error: Invalid operation '{operation}'.")
            return # Exit if the operation is invalid

        # Display the result
        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("\nError: Invalid input. Please ensure you enter only numbers.")

# Run the calculator
if __name__ == "__main__":
    simple_calculator()

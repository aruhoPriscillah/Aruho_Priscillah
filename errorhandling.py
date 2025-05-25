def get_number(prompt):
    """Prompt the user for a number and handle invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def divide_numbers():
    """Perform division of two numbers with error handling."""
    while True:
        num1 = get_number("Enter the numerator: ")
        num2 = get_number("Enter the denominator: ")
        
        try:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
            break
        except ZeroDivisionError:
            print("Error! Division by zero is invalid. Please enter a valid denominator.")

# Main program loop
if __name__ == "__main__":
    divide_numbers()

"""Interactive calculator using utils functions."""
from src.utils import add, subtract, multiply, divide


def print_menu():
    """Display the calculator menu."""
    print("\n" + "="*40)
    print("      CALCULATOR MENU")
    print("="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("="*40)


def get_numbers():
    """
    Get two numbers from user input.
    
    Returns:
        tuple: Two float numbers
        
    Raises:
        ValueError: If input is not numeric
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        raise ValueError("Invalid input. Please enter numeric values.")


def get_choice():
    """
    Get user's menu choice.
    
    Returns:
        int: User's choice (1-4)
        
    Raises:
        ValueError: If choice is not 1-4
    """
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Choice must be between 1 and 4")
        return choice
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Invalid input. Please enter a number between 1-4.")
        raise


def calculate(choice, num1, num2):
    """
    Perform calculation based on choice.
    
    Args:
        choice (int): Operation choice (1-4)
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: Result of calculation
        
    Raises:
        ZeroDivisionError: If dividing by zero
    """
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return divide(num1, num2)


def main():
    """Main calculator loop."""
    print("\nWelcome to CalcuLait - Your Python Calculator!")
    
    while True:
        try:
            print_menu()
            choice = get_choice()
            num1, num2 = get_numbers()
            
            result = calculate(choice, num1, num2)
            
            operations = {1: "Addition", 2: "Subtraction", 
                         3: "Multiplication", 4: "Division"}
            
            print(f"\n✓ {operations[choice]} Result: {num1} → {num2} = {result}")
            
        except ValueError as e:
            print(f"\n✗ Error: {e}")
        except ZeroDivisionError as e:
            print(f"\n✗ Error: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting calculator. Goodbye!")
            break
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
        
        try:
            continue_calc = input("\nDo another calculation? (y/n): ").lower()
            if continue_calc != 'y':
                print("\nThank you for using CalcuLait. Goodbye!")
                break
        except KeyboardInterrupt:
            print("\n\nExiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()

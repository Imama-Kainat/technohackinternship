# Function to display the calculator interface
def display_calculator():
    print("""
  🦋🦋🦋🦋🦋🦋🦋🦋🦋
  🦋+--------------+🦋
  🦋|  CALCULATOR  |🦋
  🦋+--------------+🦋
  🦋|  + ADD       |🦋
  🦋|  - SUBTRACT  |🦋
  🦋|  * MULTIPLY  |🦋
  🦋|  / DIVIDE    |🦋
  🦋+______________+🦋
  🦋🦋🦋🦋🦋🦋🦋🦋🦋
""")


# Infinite loop for continuous calculations
while True:
    # Display calculator interface
    display_calculator()

    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /)")
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on the operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operator"

    # Display the result with butterfly border
    print("\nResult:")
    print("🦋" * 10)
    print(f"🦋{num1} {operator} {num2} = {result}")
    print("🦋" * 10)
    # input() function use to take input from user and store in variable
    # the upper function convert input into uper case so that to became python case insensitve
    # Ask if the user wants to continue
    user_choice = input("Do you want to perform another calculation? (Y/N): ").upper()
    if user_choice != 'Y':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

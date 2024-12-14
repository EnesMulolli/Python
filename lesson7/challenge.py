def calculate(num1, num2, operator):
    # Check the operator and perform the corresponding operation
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Error: Invalid operator. Please use +, -, *, or /.")

# Main part of the program
try:
    # Get user input for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    # Call the function with user inputs and print the result
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} is: {result}")

except ValueError as ve:
    print(ve)  # Handle invalid input or invalid operator

except ZeroDivisionError as zde:
    print(zde)  # Handle division by zero error

except Exception as e:
    print(f"An unexpected error occurred: {e}")  # Handle any other unexpected errors

finally:
    print("Program execution has ended.")  # Final message indicating the end of the program


#create a function that takes 3 arguments:
# num1, num2 and operator, Inside the function ,
# use if-elif=else statements to check the operation
# and perform corresponding arthimetric. Raise a valueError if the operation is invalid.
# Outside the function, promt the user to enter 2 numbers using input() and convert the to floats.
# Promt the user to enter an arthmetic operation. Call the function with the numbers ad the  operation.
# Print the result of operation . Use try-except to handle the following excpections: a) Value error for invalid input or operation. b)
# ZeroDivisionError for division by zero. c) a general excpection for any other unexpected errors.
# d)Ensure the program prints appopriate erorr message for each excpection. use a finally block
# to print a mesage indicating the end of the program
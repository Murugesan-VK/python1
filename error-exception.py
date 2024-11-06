try:
    # Try to open a file and perform division
    file = open('example.txt', 'r')
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

finally:
    print("This block always executes, whether an exception occurred or not.")

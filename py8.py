# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Arithmetic operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handle division by zero
if num2 != 0:
    div_result = num1 / num2
    rem_result = num1 % num2
else:
    div_result = "undefined (cannot divide by zero)"
    rem_result = "undefined (cannot divide by zero)"

# Display results
print(f"\nSum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Division: {div_result}")
print(f"Remainder: {rem_result}")

# Comparison
if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The second number is greater than the first.")
else:
    print("Both numbers are equal.")

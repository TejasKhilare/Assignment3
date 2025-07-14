import math

try:
    num = float(input("Enter a number: "))
    print(f"Square root : {math.sqrt(num)}")
    print(f"Logarithm : {math.log(num)}")
    print(f"Sine : {math.sin(num)}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of number ", num, " is : ", factorial(num))

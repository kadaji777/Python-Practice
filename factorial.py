def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example
print(factorial_recursive(5))  #  120 is the output


#Base case: factorial(0) or factorial(1) is 1

#Function calls itself with a smaller number

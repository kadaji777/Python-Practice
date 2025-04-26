def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

# Example
print(sum_of_digits(1234))  # Output is 10Take the last digit using % 10

#Add it to the total

#Remove the digit using integer division // 10

#Repeat until no digits left

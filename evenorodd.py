def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example
print(check_even_odd(7))   #the output will be odd
 #Explanation
#A number is even if it’s divisible by 2 (i.e., remainder is 0).

#Use the modulus operator % to check that.

#Return the appropriate string.

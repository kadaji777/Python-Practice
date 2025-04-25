def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example
print(reverse_string("hello"))  # the output is "olleh"

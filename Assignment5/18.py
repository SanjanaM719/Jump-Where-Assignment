# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"


def swap_comma_dot(s):
    s = s.replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')
    return s

sample_string = "32.054,23"
result = swap_comma_dot(sample_string)

print(result)

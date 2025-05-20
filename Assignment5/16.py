# 16. Write a Python program to print the index of the character in a string.



def print_char_indices(s):
    for index, char in enumerate(s):
        print(f"Character: '{char}' is at index {index}")

sample_string = "hello"
print_char_indices(sample_string)

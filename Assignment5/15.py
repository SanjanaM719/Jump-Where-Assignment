# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

# Python program to count repeated characters in a string

from collections import Counter

def count_repeated_characters(s):
    char_count = Counter(s)
    

    for char, count in char_count.items():
        if count > 1:
            print(f"{char} {count}")


sample_string = 'thequickbrownfoxjumpsoverthelazydog'
count_repeated_characters(sample_string)

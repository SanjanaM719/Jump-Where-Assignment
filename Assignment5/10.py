# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


def unique_sorted_words():
    words = input("Enter a comma-separated sequence of words: ").split(',')
    
    unique_words = sorted(set(word.strip() for word in words))
    
    print(', '.join(unique_words))

unique_sorted_words()

# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


def convert_to_uppercase(s):
    count = sum(1 for char in s[:4] if char.isupper())
    
  
    if count >= 2:
        return s.upper()
    return s 

print(convert_to_uppercase("Abcdef"))  
print(convert_to_uppercase("ABcdEf"))  

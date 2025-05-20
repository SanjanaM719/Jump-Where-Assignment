# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 


def first_last_two_chars(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

print(first_last_two_chars('thisisniceone'))  
print(first_last_two_chars('ab'))            
print(first_last_two_chars('f'))              

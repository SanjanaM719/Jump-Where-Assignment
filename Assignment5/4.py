# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def change_char(s):
    if not s:
        return ''
    first_char = s[0]
   
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

print(change_char('restart'))  

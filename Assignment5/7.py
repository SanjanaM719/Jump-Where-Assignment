# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


def replace_not_poor(s):
    not_index = s.find('not')
    poor_index = s.find('poor')


    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        
        return s[:not_index] + 'good' + s[poor_index + 4:]
    return s


print(replace_not_poor('The lyrics is not that poor!'))  
print(replace_not_poor('The lyrics is poor!'))          

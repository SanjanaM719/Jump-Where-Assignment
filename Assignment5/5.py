# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'



def swap_first_two_chars(s1, s2):
  
    if len(s1) < 2 or len(s2) < 2:
        return "Both strings should have at least two characters."
    
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]

    return new_s1 + ' ' + new_s2

print(swap_first_two_chars('abc', 'xyz'))  

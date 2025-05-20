# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 


def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]  
    return s 

print(reverse_if_multiple_of_four("hello"))    
print(reverse_if_multiple_of_four("abcdefgh")) 

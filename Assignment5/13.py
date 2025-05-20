# 13. Write a Python program to check whether a string starts with specified characters.



def starts_with(s, prefix):
   
    return s.startswith(prefix)


print(starts_with("hello world", "hello")) 
print(starts_with("hello world", "world"))  

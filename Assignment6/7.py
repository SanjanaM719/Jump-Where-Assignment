# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

numbers = [10, 45, 23, 67, 89, 5, 33, 29, 31, 50]
count = 0

for num in numbers:
    if num > 30:
        count += 1

print("Number of elements greater than 30:", count)

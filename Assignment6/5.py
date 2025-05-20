# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

count = 0
total = 0

while True:
    num = int(input("Enter an integer number (0 to finish): "))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = total / count
    print("Sum:", total)
    print("Average:", average)

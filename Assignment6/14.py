# 14. Print multiplication table of 24, 50 and 29 using loop.

def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print("Multiplication table of 24:")
print_multiplication_table(24)

print("\nMultiplication table of 50:")
print_multiplication_table(50)

print("\nMultiplication table of 29:")
print_multiplication_table(29)

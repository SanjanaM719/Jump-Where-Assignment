# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

even_numbers = [num for num in range(1, 101) if num % 2 == 0]
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

divisible_by_4 = [num for num in even_numbers if num % 4 == 0]
divisible_by_6 = [num for num in even_numbers if num % 6 == 0]
divisible_by_8 = [num for num in even_numbers if num % 8 == 0]
divisible_by_10 = [num for num in even_numbers if num % 10 == 0]
divisible_by_3 = [num for num in even_numbers if num % 3 == 0]
divisible_by_5 = [num for num in even_numbers if num % 5 == 0]
divisible_by_7 = [num for num in even_numbers if num % 7 == 0]
divisible_by_9 = [num for num in even_numbers if num % 9 == 0]

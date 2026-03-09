# 3.Find the largest number using a for loop.
# numbers = [100, 25, 7, 92, 18, 3, 50]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print("Largest number among is : ", largest)

# 4.Calculate the factorial of a number using a for loop.
# n = int(input("Enter number to get its factorial : "))
# factorial = 1
# for i in range(n, 0, -1):
#     factorial = i * factorial
# print(factorial)

# 5.Check whether a number is prime using a for loop.
# while(1):
#     num = int(input("Enter your number:"))
#     if num < 2:
#         result = "Invalid input"
#     else:
#         result = "Prime"
#         for i in range(2,num):
#             if num % i == 0:
#                 result = "not prime"
#                 break
#     print(result)

# 6.Count the number of vowels in:
# text = "Hello Python Programming"
# count = 0
# for ch in text.lower():
#     if ch in "aeiou":
#         count = count + 1
# print(count)

# 7.Count the number of uppercase and lowercase characters in a string.
# text = input("Enter text : ")
# lowercase_ch = 0
# uppercase_ch = 0

# for ch in text:
#     if ch.isupper():
#         uppercase_ch += 1
#     elif ch.islower():
#         lowercase_ch += 1
# print("lowercase_ch = ",lowercase_ch)
# print("uppercase_ch = ",uppercase_ch)

# 8.Reverse a string using a for loop without using [::-1].
# text = input("Enter text : ")
# reverse_text = ""
# for ch in text:
#     reverse_text = ch + reverse_text
# print(reverse_text)

# 10.Find the second-largest number in a list using a for loop.
# numbers = [10, 25, 50, 2, 18, 3, 39]
# largest_no = numbers[0]
# second_largest_no = numbers[0]
# for number in numbers:
#     if number > largest_no:
#         second_largest_no = largest_no
#         largest_no = number
#     elif number > second_largest_no and number != largest_no:
#         second_largest_no = number

# print("largest_no : ", largest_no)
# print("second_largest_no : ", second_largest_no)


# 11.Print this pattern:
# *
# **
# ***
# ****
# *****
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# 12.Print:
# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 13.Print:
# 54321
# 5432
# 543
# 54
# 5
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

# 14.Print a 5 × 5 square:
# *****
# *****
# *****
# *****
# *****
# for i in range(1,6):
#     print("*" * 5)

# 15.Print multiplication tables from 1 to 10 using nested for loops.
# for i in range(1, 11):
#     print(f"Multiplication table of {i}:")
#     for j in range(1, 11):
#         print(f"{i} X {j} = {i * j}")

# 29.Find all prime numbers between 1 and 100.
# prime_no = []
# for i in range(2, 101):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         prime_no.append(i)
# print(prime_no)

# 30.Print the Fibonacci series up to 10 terms using a for loop.
# fib = []
# for i in range(10):
#     if i == 0 or i == 1:
#         fib.append(i)
#     else:
#         # fib[i] = fib[i - 1] + fib[i - 2]
#         fib.append(fib[i - 1] + fib[i - 2])
# print(fib)

# 31.Find the frequency of each character in:
# text = "programming"
# frequency = {}

# for ch in text:
#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1
# print(frequency)

# 32.Remove duplicate elements from a list without using set().
# text = "programming"
# print("original string with uplicates:",text)
# unique = ""
# for ch in text:
#     if ch not in unique:
#         unique += ch
# text = unique
# print("new string with only unique character:",text)

# 33.Find the common elements between two lists using for loops.
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 6, 7, 2, 8]
# common_ele = []
# for i in l1:
#     if i in l2:
#         common_ele.append(i)
# print(common_ele)

# 34.Find whether a number is an Armstrong number using a for loop.
# number = "154"
# total = 0
# for i in number:
#     sum += int(i) ** len(number)
# print("Sum of the number is:",sum)
# if int(number) == sum:
#     print(f"{number} is an armstrong number")
# else:
#     print(f"{number} is not an armstrong number")
    

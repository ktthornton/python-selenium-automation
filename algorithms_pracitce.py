# -----swapping variables-----
# time complexity is O(1) - linear
# example using stored
# def swap_variables(a:int, b:int):
#     print(f'original: a = {a}, b = {b}')
#     a,b = b, a
#     print(f'swapped: a = {a}, b = {b}')
#

# test_a1 = 5
# test_b1 = 10
# swap_variables(test_a1, test_b1)

# example storing in a temp variable
# def swap_variables2(a:int, b:int):
#     print(f'original: a = {a}, b = {b}')
#     #need to fill in this code for reference from the slides
#     print(f'swapped: a = {a}, b = {b}')


# using math
# def swap_variables3(a:int, b:int):
#     print(f'original: a = {a}, b = {b}')
#     a = a + b
#     b = a - b
#     a = a -b
#     print(f'swapped: a = {a}, b = {b}')
#
#
# test_a3 = 5
# test_b3 = 10
# swap_variables3(test_a3, test_b3)


# ----- fizz buzz -----
# time complexity is O(n)
# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 5 == 0:
#             print('buzz')
#         elif i % 3 == 0:
#             print('fizz')
#         else:
#             print(i)


# fizz_buzz()

# alternate - set a variable in the range and define the variable when calling the function
# def fizz_buzz2(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 5 == 0:
#             print('buzz')
#         elif i % 3 == 0:
#             print('fizz')
#         else:
#             print(i)
#
#
# fizz_buzz2(19)

# ----- factorial -----
# time complexity is O(n)
# def factorial_calc(n:int):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     print(f'The factorial of {n} is {result}')


# factorial_calc(5)


# ----- sum of 3 digit number -----
# time complexity is O(n)

# using floor division
# def sum_of_three(number: int):
#     result = 0
#     for i in range(3):
#         result = result + (number % 10)
#         number = number // 10
#     return result
#
#
# test_result = sum_of_three(123)
# print(test_result)


# ---- reverse string -----
# time complexity is O1
# def reverse_string(string: str):
#     return string[::-1]
#
#
# print(reverse_string('abcde'))


# ----- reverse integer -----
# time complexity is O1
# def reverse_negative_number(number: int):
#     string = str(number)
#     if string[0] == '-':
#         return int("-" + (string[:0:-1]))
#     else:
#         return int(string[::-1])
#
#
# print(reverse_negative_number(-123))
# print(reverse_negative_number(456))


# --- anagram ---
# time complexity is O1
# def is_anagram(s1: str, s2: str):
#     if len(s1) != len(s2):
#         return False
#     elif sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
#
#
# print(is_anagram("cat", "act"))
# print(is_anagram("test", "set"))
# print(is_anagram("map", "sap"))


# --- palindrome ---
# time complexity is O1
# def is_palindrome(s1: str):
#     if s1 == s1[::-1]:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome('madam'))
# print(is_palindrome('common'))
# print(is_palindrome('tacocat'))


# --- almost a palindrome ---
# rakdar - true
# radario - false

# def almost_palindrome(s: str):
#     word = len(s)
#     # word_2 = 0
#     for i in range(word):
#         new_s = s[:i] + s[i + 1:]
#         if new_s == new_s[::-1]:
#             return True
#     return False
#
#
# print(almost_palindrome("rakdar"))
# print(almost_palindrome("rakidar"))

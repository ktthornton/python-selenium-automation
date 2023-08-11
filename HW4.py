#scenario 3/HW problem 4- Kata exercise
random_number = 1234567890


def reverse_number_function(num):
    num = str(num)
    reverse_number = []
    for i in num:
        num = int(num)
        reverse_number.append(i)
        reverse_sort = reverse_number[::-1]
    return reverse_sort


print(reverse_number_function(random_number))

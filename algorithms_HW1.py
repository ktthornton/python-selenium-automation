# Level 1 #1 BinGo practice - pre-code given in HW looks like it's asking for Foo/Bar, I'm using Bin/Go below from the
# steps that were outlined
def foo_bar():
    for i in range(1, 101):
        if i % 3 == 0 and i % 7 == 0:  # Check if the number is divisible by 3 and 7 and print 'BinGo'
            print('BinGo')
        elif i % 3 == 0:  # Check if the number is divisible by 3 and print 'Bar'
            print('Bin')
        elif i % 7 == 0:  # Check if the number is divisible by 7 and print 'Go'
            print('Go')
        else:
            print(i)


print(foo_bar())


# Level 1 #2 sum of digits 1 to n
def sum_numbers(n: int):
    # Initialize the variable 'final_sum' and set it to 0 initially
    final_sum = 0

    # Use a loop to iterate over numbers from 0 to n (inclusive)
    for i in range(n + 1):
        # Count the sum of digits for each iteration
        final_sum = final_sum + i
    # Return the 'final_sum' as the result
    return final_sum


print(sum_numbers(5))


# Level 2 #1 max number
def find_max(a: int, b: int, c: int):
    # compare a to b and c
    if (a >= b) and (a >= c):
        print(a)
    # compare b to a and c
    elif (b >= a) and (b >= c):
        print(b)
    # compare c to a and b
    elif (c >= a) and (c >= b):
        print(c)


find_max(1, 2, 3)


# Level 2 #2 leap year
def leap_year(year: int):
    if ((year % 400 == 0) or
        (year % 100 != 0) and
         (year % 4 == 0)):
        return 'True'
    else:
        return 'False'


print(leap_year(2012))


# Level 2 #3 Fibonacci
def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):

        # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
        fib_number = fib_sequence[-1] + fib_sequence[-2]

        # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(fib_number)
    return fib_sequence


print(generate_fibonacci_sequence(7))

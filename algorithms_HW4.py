# #1 sum of even and product of odd numbers
def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1
    for number in arr:
        if number % 2 == 0:
            sum_even += number
        elif number % 2 != 0:
            product_odd *= number
    return [sum_even, product_odd]


print(sum_even_and_product_odd([1, 2, 3, 4]))


# #2 sum between range values
def sum_between_range(arr: list, min_val: int, max_val: int):
    range_sum = 0
    for number in range(len(arr)):
        if number in arr[min_val:max_val + 1]:
            range_sum += number
    return range_sum


print(sum_between_range([3, 2, 1, 4, 10, 8, 7, 6, 9, 5], 3, 7))


# #3 stock price
# Define a function that takes a list of stock prices as its argument
def buy_and_sell_stock(prices: list):
    # Initialize the variable 'maximum' to store the maximum profit, starting at 0
    maximum = 0
    # Loop through the list of prices; stop one element before the last to avoid index out-of-bounds
    for number in range(len(prices) - 1):
        # Check if the next day's price is higher than the current day's
        if prices[number + 1] > prices[number]:
            # If it is, add the difference between the two prices to 'maximum'
            maximum += (prices[number + 1] - prices[number])
    # Return the calculated maximum profit after the loop ends
    return maximum


print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))

# #4 increment a number
# def plus_one(arr: list):
#     # Add 1 to the last digit of the number
#     arr[-1] += 1
#
#     # Loop through the array in reverse, starting from the second last element
#     for i in reversed(range(1, len(arr))):
#
#         # If the current digit is not 10, there's no carry-over, and we can break the loop
#         if arr[i] != 10:
#             break

    # Set the current digit to 0 because we have a carry-over

    # Add 1 to the preceding digit (i-1) to handle the carry-over

    # Check if the most significant digit (first digit) has a carry-over

    # Set the first digit to 1

    # Append a 0 to the array to handle the carry-over from the most significant digit

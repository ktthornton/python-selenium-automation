# task #1
def find_two_lowest(arr: list):
    arr.sort()
    return arr[0:2]


print(find_two_lowest([198, 3, 4, 9, 10, 9, 2]))
print(find_two_lowest([10, 100, -100, 53, 0]))


# task 2
def invert_list(arr: list):
    inverted_list = []
# Loop through each index of the array
    for i in arr:
        i = str(i)
        if '-' in i:
            inverted_list.append(int(i[1::]))
        else:
            inverted_list.append(int('-' + i))
    return inverted_list


print(invert_list([1, 5, -2, 4]))
print(invert_list([-10, -12, 14, 16, 0]))


# task 3
def max_diff(arr: list):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0
    else:
        arr.sort()
        result = arr[-1] - arr[0]
        return result
# Sort the list in ascending order
# After sorting, the smallest element will be at index 0,
# and the largest will be at the last index
# Calculate and return the difference between the largest and smallest elements
# Use indexes of the elements


print(max_diff([3, 5, 7, 2]))
print(max_diff([100, -11, 0, 1]))
print(max_diff([]))


# task 4
def count_larger_neighbors(arr: list):
    # Initialize a variable 'count' to 0. This variable will keep track of the number of elements
    # that are larger than both their adjacent neighbors.
    count = 0

    # Loop through the list from index 1 to len(arr) - 2. We skip the first and the last elements
    # because they don't have both left and right neighbors.
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1]:
            count += 1
# Check if the current element (arr[i]) is greater than its left neighbor (arr[i - 1])
# and its right neighbor (arr[i + 1]).
# If the condition is met, increment the 'count' variable by 1.
    return count

# Return the final count of elements that are larger than both their neighbors.


print(count_larger_neighbors([2, 56, 7, 21, 22, 19, 26]))


# task 5
def subtract_min(arr: list):
    new_list = []
# Find the minimum element in the list using the 'min' function and store it in 'min_element'.
    min_element = min(arr)
    for i in arr:
        new_list.append(i - min_element)
    return new_list


print(subtract_min([9, 2, 5, 4, 7, 6, 1]))
print(subtract_min([10, 20, 30, 40, 50]))

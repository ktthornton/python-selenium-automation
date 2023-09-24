# #1 selection sort
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


selection_list = [8, 19, 12, 3, 1, -7, 0]
print(selection_sort(selection_list))


# #2 bubble sort
def bubble_sort_descending(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


bubble_list = [8, 19, 12, 3, 1, -7, 0]
print(bubble_sort_descending(bubble_list))


# #3 insertion sort
def insertion_sort_descending(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


insertion_list = [8, 19, 12, 3, 1, -7, 0]
print(insertion_sort_descending(insertion_list))

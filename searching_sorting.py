# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"{target} found at index {mid}!"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"{target} not found in the list."

# Sample list of numbers
numbers = [23, 5, 12, 56, 9, 78, 34, 1, 4]

# Sorting the list using Quick Sort
sorted_numbers = quick_sort(numbers)
print("Sorted List:", sorted_numbers)

# Searching for a number using Binary Search
search_result = binary_search(sorted_numbers, 12)  # Searching for the number 12
print(search_result)

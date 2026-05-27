"""
1. - Binary Search checks the middle element and halves the search range until the target is found.

Algorithm :
1. Set low = 0 and high = len(arr) - 1.
2. While low <= high:
   a. Compute mid = (low + high) // 2.
   b. If arr[mid] == target -> return mid.
   c. If arr[mid] < target -> set low = mid + 1.
   d. Else -> set high = mid - 1.
3. If not found -> return -1.

"""

def Binary_Search(arr, t_val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == t_val:
            return mid
        elif arr[mid] < t_val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data = [1, 2, 3, 4, 5.5, 6, 7, 8, 8.9, 9, 10]
print("Enter the target value:")
t_val = float(input())
result = Binary_Search(data, t_val)
print(f"Index of {t_val}: {result}")
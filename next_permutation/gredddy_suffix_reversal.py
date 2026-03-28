
def nextPermutation(arr):
    n = len(arr)

    # 1. Find pivot (first element from right where arr[i] < arr[i+1])
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # 2. If pivot exists, find successor and swap
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    # 3. Reverse the suffix
    arr[i + 1:] = reversed(arr[i + 1:])


# Driver code
arr = [2, 4, 1, 7, 5, 0]
nextPermutation(arr)
print(arr)



def nextPermutation(arr):
    n = len(arr)

    # Step 1: Find pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # If pivot not found, array is in descending order
    if pivot == -1:
        arr.sort()     # O(n^2) sort
        return

    # Step 2: Find the smallest element greater than pivot
    successor = -1
    for i in range(pivot + 1, n):
        if arr[i] > arrif successor == -1 or arr[i] < arrsuccessor = i

    # Step 3: Swap pivot and successor
    arr[pivot], arr[successor] = arr[successor], arr[pivot]

    # Step 4: Sort suffix using bubble sort (O(n^2))
    for i in range(pivot + 1, n):
        for j in range(i + 1, n):
            if arr[i] > arrarr[i], arr[j] = arr[j], arr[i]


# Driver code
arr = [2, 4, 1, 7, 5, 0]
nextPermutation(arr)
print(arr)

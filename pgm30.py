def sort_array(arr):
    n = len(arr)

    # Loop through all elements
    for i in range(n):
        # Compare
        for j in range(i + 1, n):
            if arr[i] > arr[j]:  #Swap
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", sort_array(arr))
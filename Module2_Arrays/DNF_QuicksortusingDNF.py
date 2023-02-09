def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end


def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)
    return arr


def quickSortUsingDutchNationalFlag(arr):
    quickSort(arr, 0, len(arr)-1)
    return arr


arr = [1, 4, 4, 3, 3]
print(quickSortUsingDutchNationalFlag(arr))

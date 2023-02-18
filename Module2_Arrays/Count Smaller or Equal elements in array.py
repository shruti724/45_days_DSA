def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def countSmallerOrEqual(a, b, n, m):
    x = []
    y = []

    for i in range(n):
        x.append(a[i])

    for j in range(m):
        y.append(b[j])

    i = 0
    j = 0
    count = 0
    ans = []
    while (i < n) and (j < m):
        if x[i] >= y[j]:
            count += 1
            ans.append(count)
            j += 1
        else:
            count = 0
            ans.append(count)
        i += 1


    return ans


arr_a = [5, 4, 3, 2, 1]
n = len(arr_a)
arr_b = [3, 4]
m = len(arr_b)
print(countSmallerOrEqual(arr_a, arr_b, n, m))

# 2 2 1 0 0
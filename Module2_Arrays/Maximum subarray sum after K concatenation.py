def maxSubSumKConcat(arr, n, k):
    li = []
    curr_sum = 0
    max_sum = 0
    for i in range(n):
        li.append(arr[i])

    new_li = li * k

    for j in range(len(new_li)):
        curr_sum = curr_sum + new_li[j]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

    pass

arr = [1, 3]
n = len(arr)
k = 3
print(maxSubSumKConcat(arr, n, k))
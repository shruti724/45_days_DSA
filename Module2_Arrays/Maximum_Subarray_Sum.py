def maxSubarraySum(arr, n):
    curr_sum = 0
    max_sum = 0

    for i in range(n):
        curr_sum = curr_sum + arr[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


arr = [2. -10, 0, 90]
n = len(arr)
print(maxSubarraySum(arr, n))

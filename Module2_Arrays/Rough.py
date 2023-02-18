# def fun(arr, n):
#     low = 0
#     mid = 0
#     high = n - 1
#     while mid <= high:
#         if arr[mid] == 0:
#
#
#
# arr = [1, 0, 0, 2, 2]
# n = len(arr)

# swap function

# def swap(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b


# print(swap(4, 5))

# def sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] < arr[j]:
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#     return arr
#
#
# arr = [1, 4, 2, 6]
# print(sort(arr))

# a = -12
# b = -32
# ans = max(a, b)
# print(ans)

# arr = [-12, -4, -34]
# ans = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             ans = max(arr[i], arr[j])
# print(ans)

# def convertString(str):
#     n = len(str)
#     s = ""
#     i = 0
#     while i < n:
#         if str[i] != " ":
#             s = s + str[i]
#             i += 1
#         else:
#             s = s + " " + str[i+1].upper()
#             i += 1
#     return s
#
#
# str = "I love you python"
# print(convertString(str))

def findNonRepeating(str):
    count = 1
    n = len(str)
    i = 0
    j = i + 1
    while i < n:
        while j < n:
            if str[i] == str[j]:
                count += 1
            j += 1
        i += 1
    return count


str = "babaabea"
print(findNonRepeating(str))
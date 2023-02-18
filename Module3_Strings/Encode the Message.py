# def encode(message):
#     count = 1
#     count_arr = ""
#     n = len(message)
#     i = 0
#
#     while i < n:
#         j = i + 1
#         while j < n:
#             if message[i] == message[j]:
#                 count += 1
#             j += 1
#         if message[i] in count_arr:
#             pass
#         else:
#             count_arr = count_arr + message[i]
#             count_arr = count_arr + str(count)
#             count = 1
#         i += 1
#
#
#     return count_arr
#
#
# str1 = "aabbc"
# print(encode(str1))

# input:
# 3
# aabbc
# abcd
# abbdcaas

# output
# a2b2c1
# a1b1c1d1
# a1b2d1c1a2s1


def encode(message):
    n = len(message)
    count = 1
    count_arr = ""
    for i in range(n):
        for j in range(n):
            if message[i] == message[j]:
                count += 1
    return count_arr

str1 = "aabbc"
print(encode(str1))

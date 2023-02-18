def findNonRepeating(str):
    hashmap = {}
    for i in str:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    # for j in str:
    #     if hashmap[j] == 1:
    #         return j
    return hashmap
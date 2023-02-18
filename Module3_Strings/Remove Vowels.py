def removeVowels(inputString):
    str = inputString
    n = len(str)
    ans = ""
    for i in range(n):
        if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
            pass
        elif str[i] == "A" or str[i] == "E" or str[i] == "I" or str[i] == "O" or str[i] == "U":
            pass
        else:
            ans = ans + str[i]

    return ans


str = "Coding Ninjas"
print(removeVowels(str))

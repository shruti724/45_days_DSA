def convertString(str):
    return ' '.join(map(lambda x: x[0].upper()+x[1:], str.split()))

str = "i love python"
print(convertString(str))
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    result = 0
    for i in range(a + 1, b):
        if i not in tup:
            result += i
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()
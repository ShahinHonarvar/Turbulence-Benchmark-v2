def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    result = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in t:
            result -= i
    if result % 2 == 1:
        return bin(result)[2:]
    elif result != 0:
        return hex(result)[2:].upper()
    else:
        return ''
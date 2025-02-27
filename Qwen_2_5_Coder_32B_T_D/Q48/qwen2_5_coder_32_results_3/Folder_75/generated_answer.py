def return_binary_or_hexa(data):
    a = data[20]
    b = data[51]
    total = 0
    in_range = set(data[21:51])
    for i in range(a + 1, b):
        if i not in in_range:
            total += i
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]
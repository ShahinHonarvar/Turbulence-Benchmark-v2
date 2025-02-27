def return_binary_or_hexa(data):
    a = data[32]
    b = data[99]
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in data:
            sum_missing += i
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:] if sum_missing > 0 else ''
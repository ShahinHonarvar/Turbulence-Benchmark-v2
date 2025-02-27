def return_binary_or_hexa(data):
    a = data[275]
    b = data[871]
    sum_missing = sum(set(range(a + 1, b)) - set(data[276:871]))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
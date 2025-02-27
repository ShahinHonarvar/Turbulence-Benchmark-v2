def return_binary_or_hexa(data):
    a = data[56]
    b = data[88]
    sum_missing = sum(set(range(a + 1, b)) - set(data[57:88]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
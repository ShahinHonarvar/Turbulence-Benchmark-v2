def return_binary_or_hexa(tup):
    a, b = (tup[30], tup[200])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in tup[30:200]))
    if sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]
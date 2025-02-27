def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    nums_present = set(tup[a + 1:b])
    sum_absent = sum(set(range(a + 1, b)) - nums_present)
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]
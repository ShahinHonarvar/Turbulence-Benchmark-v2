def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_missing += i
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].rstrip('L')
    else:
        return bin(sum_of_missing)[2:]
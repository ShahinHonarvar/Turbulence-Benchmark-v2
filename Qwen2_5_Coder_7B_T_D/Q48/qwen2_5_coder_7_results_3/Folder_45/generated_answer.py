def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in tup[30:201]:
            sum_val += i
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
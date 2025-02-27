def return_binary_or_hexa(tup):
    sum_val = 0
    for i in range(tup[0] + 1, tup[7]):
        if i not in tup:
            sum_val += i
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
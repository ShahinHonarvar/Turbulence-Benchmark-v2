def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[8])
    sum_val = 0
    for num in range(a + 1, b):
        if num not in tup[2:9]:
            sum_val += num
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    elif sum_val % 2 == 0 and sum_val != 0:
        return hex(sum_val)[2:]
    return ''
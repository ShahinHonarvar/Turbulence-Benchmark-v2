def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    sum_val = 0
    present_numbers = set(tup[31:200])
    for num in range(a + 1, b):
        if num not in present_numbers:
            sum_val += num
    if sum_val == 0:
        return ''
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]
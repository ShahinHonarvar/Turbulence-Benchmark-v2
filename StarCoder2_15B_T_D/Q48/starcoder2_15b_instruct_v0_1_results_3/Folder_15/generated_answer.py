def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[4]
    lst = list(range(a + 1, b))
    remaining = [num for num in lst if num not in tup]
    if not remaining:
        return ''
    sum_val = sum(remaining)
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
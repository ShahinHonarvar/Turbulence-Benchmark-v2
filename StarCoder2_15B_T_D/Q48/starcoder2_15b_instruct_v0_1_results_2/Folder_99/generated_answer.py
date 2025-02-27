def return_binary_or_hexa(tup: tuple) -> str:
    try:
        a = tup[427]
        b = tup[669]
    except IndexError:
        return ''
    sum_val = 0
    for num in range(a + 1, b):
        if num not in tup:
            sum_val += num
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
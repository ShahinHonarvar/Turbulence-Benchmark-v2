def return_binary_or_hexa(tup):
    a, _, b = tup
    if a == b - 1:
        return ''
    sum_of_missing_ints = sum(range(a + 1, b)) - sum(tup[1:-1])
    if sum_of_missing_ints % 2 == 1:
        return bin(sum_of_missing_ints)[2:]
    else:
        return hex(sum_of_missing_ints)[2:].upper()
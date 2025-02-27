def return_binary_or_hexa(tup: tuple) -> str:
    if len(tup) < 3:
        return ''
    a, b = (tup[0], tup[2])
    sum_of_missing = sum(range(a + 1, b)) - sum(tup[1:3])
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]
def return_binary_or_hexa(tup: tuple) -> str:
    a, b = (tup[18], tup[52])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in tup[18:52]))
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing).lstrip('0b')
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing).lstrip('0x')
    else:
        return ''
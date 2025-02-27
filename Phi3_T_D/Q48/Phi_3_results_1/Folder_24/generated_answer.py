def return_binary_or_hexa(arr_tuple):
    a = arr_tuple[13]
    b = arr_tuple[91]
    sum_missing = sum(set(range(a + 1, b)).difference(arr_tuple[13:92]))
    if sum_missing:
        if sum_missing % 2 != 0:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
    return ''
def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[15], sorted_tuple[57])
    missing_sum = sum((i for i in range(a + 1, b) if i not in sorted_tuple))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return '{:b}'.format(missing_sum)
def return_binary_or_hexa(integers):
    a = integers[56]
    b = integers[88]
    missing_sum = sum((x for x in range(a + 1, b) if x not in integers[56:89]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return hex(missing_sum)[2:].upper()
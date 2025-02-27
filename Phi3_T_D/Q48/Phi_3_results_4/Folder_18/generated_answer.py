def return_binary_or_hexa(integers):
    a, b = (integers[56], integers[90])
    missing_sum = sum((x for x in range(a + 1, b) if x not in integers[56:90]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
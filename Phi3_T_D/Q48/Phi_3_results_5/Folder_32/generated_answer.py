def return_binary_or_hexa(integers):
    a = integers[86]
    b = integers[90]
    absent_sum = sum((x for x in range(a + 1, b) if x not in integers[86:90]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:].upper()
    else:
        return bin(absent_sum)[2:]
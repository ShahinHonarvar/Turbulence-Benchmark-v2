def return_binary_or_hexa(integers):
    if len(integers) < 97:
        return ''
    a = integers[90]
    b = integers[97]
    missing_sum = sum((i for i in range(a + 1, b) if i not in integers[90:97]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
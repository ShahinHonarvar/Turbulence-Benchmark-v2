def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[42:88]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
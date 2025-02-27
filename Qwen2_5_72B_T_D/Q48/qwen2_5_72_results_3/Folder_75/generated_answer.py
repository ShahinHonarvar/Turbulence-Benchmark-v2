def return_binary_or_hexa(data):
    a = data[20]
    b = data[51]
    missing_sum = sum(set(range(a + 1, b)) - set(data[21:51]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
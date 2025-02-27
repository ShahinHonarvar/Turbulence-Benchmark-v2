def return_binary_or_hexa(data):
    a = data[86]
    b = data[90]
    missing_sum = sum(set(range(a + 1, b)) - set(data[87:90]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]
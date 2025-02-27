def return_binary_or_hexa(data):
    a = data[57]
    b = data[84]
    missing_sum = sum(set(range(a + 1, b)) - set(data[58:84]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(data):
    a = data[29]
    b = data[53]
    missing_sum = sum(set(range(a + 1, b)) - set(data[30:53]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
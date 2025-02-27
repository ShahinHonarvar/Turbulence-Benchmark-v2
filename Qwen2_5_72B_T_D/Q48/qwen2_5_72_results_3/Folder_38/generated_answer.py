def return_binary_or_hexa(data):
    a = data[36]
    b = data[85]
    missing_sum = sum(set(range(a + 1, b)) - set(data[37:85]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
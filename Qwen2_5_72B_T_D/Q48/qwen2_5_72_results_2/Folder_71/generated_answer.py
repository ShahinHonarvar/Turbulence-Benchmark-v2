def return_binary_or_hexa(data):
    a = data[20]
    b = data[35]
    missing_sum = sum(set(range(a + 1, b)) - set(data[21:35]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
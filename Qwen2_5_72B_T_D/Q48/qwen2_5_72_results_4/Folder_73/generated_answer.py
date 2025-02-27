def return_binary_or_hexa(data):
    a = data[10]
    b = data[76]
    missing_sum = sum(set(range(a + 1, b)) - set(data[11:76]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
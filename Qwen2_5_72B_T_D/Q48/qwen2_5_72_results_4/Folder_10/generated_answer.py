def return_binary_or_hexa(data):
    a = data[36]
    b = data[54]
    missing_sum = sum(set(range(a + 1, b)) - set(data[37:54]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
def return_binary_or_hexa(data):
    a = data[80]
    b = data[200]
    missing_sum = sum(set(range(a + 1, b)) - set(data[81:200]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
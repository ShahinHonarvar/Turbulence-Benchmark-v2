def return_binary_or_hexa(data):
    a = data[10]
    b = data[28]
    missing_sum = sum(set(range(a + 1, b)) - set(data[11:28]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
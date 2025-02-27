def return_binary_or_hexa(data):
    a = data[81]
    b = data[86]
    missing_sum = sum((i for i in range(a + 1, b) if i not in data[81:86 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return f'{bin(missing_sum)[2:]}'
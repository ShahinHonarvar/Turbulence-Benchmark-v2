def return_binary_or_hexa(data):
    a = data[49]
    b = data[74]
    missing_sum = sum(set(range(a + 1, b)) - set(data[50:74]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(data):
    a = data[11]
    b = data[76]
    subset = set(data[11:77])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
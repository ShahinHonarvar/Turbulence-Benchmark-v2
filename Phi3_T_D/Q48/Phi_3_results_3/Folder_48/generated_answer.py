def return_binary_or_hexa(data):
    a, b = (data[933], data[996])
    missing_sum = sum(set(range(a + 1, b)).difference(data[933:997]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
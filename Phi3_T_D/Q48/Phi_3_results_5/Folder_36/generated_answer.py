def return_binary_or_hexa(data):
    a, b = (data[110], data[348])
    missing_sum = sum(set(range(a + 1, b)) - set(data[110:348 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
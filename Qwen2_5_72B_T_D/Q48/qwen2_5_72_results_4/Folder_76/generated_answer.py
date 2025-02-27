def return_binary_or_hexa(data):
    a = data[450]
    b = data[905]
    missing_sum = sum(set(range(a + 1, b)) - set(data[451:905]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
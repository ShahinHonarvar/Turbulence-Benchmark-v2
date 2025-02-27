def return_binary_or_hexa(data):
    a = data[20]
    b = data[43]
    existing_values = set(data[21:43])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_values))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
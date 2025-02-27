def return_binary_or_hexa(data):
    a = data[44]
    b = data[67]
    existing_values = set(data[45:67])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_values))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
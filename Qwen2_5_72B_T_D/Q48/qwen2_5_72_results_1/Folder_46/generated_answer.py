def return_binary_or_hexa(data):
    a = data[10]
    b = data[79]
    existing_numbers = set(data[10:80])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
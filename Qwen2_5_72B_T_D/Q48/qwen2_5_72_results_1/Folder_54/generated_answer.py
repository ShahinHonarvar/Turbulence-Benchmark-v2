def return_binary_or_hexa(data):
    if len(data) < 65:
        return ''
    a, b = (data[35], data[64])
    missing_sum = 0
    existing_values = set(data[36:64])
    for number in range(a + 1, b):
        if number not in existing_values:
            missing_sum += number
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
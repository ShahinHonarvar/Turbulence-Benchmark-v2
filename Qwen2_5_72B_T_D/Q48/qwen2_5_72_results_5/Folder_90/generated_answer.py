def return_binary_or_hexa(data):
    a = data[60]
    b = data[90]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data:
            missing_sum += num
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
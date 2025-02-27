def return_binary_or_hexa(data):
    if len(data) < 92:
        return ''
    a = data[13]
    b = data[91]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data:
            missing_sum += num
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
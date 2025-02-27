def return_binary_or_hexa(data):
    if len(data) < 98:
        return ''
    a = data[90]
    b = data[97]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in data[91:97]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
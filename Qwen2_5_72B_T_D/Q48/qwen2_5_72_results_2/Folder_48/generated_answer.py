def return_binary_or_hexa(data):
    a = data[933]
    b = data[996]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data[934:996]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
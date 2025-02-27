def return_binary_or_hexa(data):
    a = data[450]
    b = data[905]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data[451:905]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
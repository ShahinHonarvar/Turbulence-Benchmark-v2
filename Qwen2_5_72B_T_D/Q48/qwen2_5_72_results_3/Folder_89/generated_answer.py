def return_binary_or_hexa(data):
    a = data[55]
    b = data[84]
    missing_sum = 0
    data_set = set(data)
    for num in range(a + 1, b):
        if num not in data_set:
            missing_sum += num
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
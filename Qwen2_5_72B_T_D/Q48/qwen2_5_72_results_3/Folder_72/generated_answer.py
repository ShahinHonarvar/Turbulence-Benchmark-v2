def return_binary_or_hexa(data):
    a, b = (data[13], data[70])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in data[14:70]:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
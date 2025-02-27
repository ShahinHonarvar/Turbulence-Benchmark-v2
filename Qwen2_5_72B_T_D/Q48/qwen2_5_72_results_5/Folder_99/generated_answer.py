def return_binary_or_hexa(data):
    a = data[427]
    b = data[669]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in data[428:669]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]
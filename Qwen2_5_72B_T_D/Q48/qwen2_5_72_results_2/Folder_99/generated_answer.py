def return_binary_or_hexa(data):
    a = data[427]
    b = data[669]
    missing_sum = sum((num for num in range(a + 1, b) if num not in data[428:669]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
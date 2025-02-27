def return_binary_or_hexa(data):
    a = data[44]
    b = data[78]
    present_numbers = set(data[45:78])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
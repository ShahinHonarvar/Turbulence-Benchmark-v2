def return_binary_or_hexa(data):
    a = data[56]
    b = data[90]
    present_numbers = set(data[57:90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
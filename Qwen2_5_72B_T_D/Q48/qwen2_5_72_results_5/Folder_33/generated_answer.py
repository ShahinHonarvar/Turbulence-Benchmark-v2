def return_binary_or_hexa(data):
    a = data[13]
    b = data[35]
    present_numbers = set(data[14:35])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
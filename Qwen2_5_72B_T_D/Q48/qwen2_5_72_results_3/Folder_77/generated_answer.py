def return_binary_or_hexa(data):
    a = data[18]
    b = data[52]
    existing_numbers = set(data[19:52])
    missing_sum = sum((x for x in range(a + 1, b) if x not in existing_numbers))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
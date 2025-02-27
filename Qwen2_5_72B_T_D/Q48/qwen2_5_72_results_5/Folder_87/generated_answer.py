def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[43]
    existing_numbers = set(tup[21:43])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
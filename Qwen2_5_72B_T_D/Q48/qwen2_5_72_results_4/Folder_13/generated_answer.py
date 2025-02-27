def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    existing_numbers = set(tup[46:92])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
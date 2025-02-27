def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(t[a + 1:b])
    actual_sum = sum(missing_numbers)
    if actual_sum % 2 == 1:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:].upper()
def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    expected_range = set(range(a + 1, b))
    actual_range = set(t[39:81])
    missing_numbers = expected_range - actual_range
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
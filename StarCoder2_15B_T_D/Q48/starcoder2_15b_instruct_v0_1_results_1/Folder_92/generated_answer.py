def return_binary_or_hexa(num_tuple):
    a, _, b = num_tuple
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum(num_tuple[1:-1])
    if actual_sum % 2 == 1:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:].upper()
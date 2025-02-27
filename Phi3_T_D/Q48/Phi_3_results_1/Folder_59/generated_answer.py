def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[0], input_tuple[10])
    expected_set = set(range(a + 1, b))
    existing_set = set(input_tuple[1:11])
    missing_set = expected_set - existing_set
    missing_sum = sum(missing_set)
    if missing_sum:
        if missing_sum % 2 == 0:
            return hex(missing_sum)[2:]
        else:
            return bin(missing_sum)[2:]
    else:
        return ''
def return_binary_or_hexa(input_tuple):
    a, _, _, b = input_tuple
    missing_sum = sum(range(a + 1, b)) - sum(input_tuple[1:4])
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
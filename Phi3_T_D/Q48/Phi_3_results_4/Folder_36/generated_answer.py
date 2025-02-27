def return_binary_or_hexa(input_tuple):
    a = input_tuple[110]
    b = input_tuple[348]
    present_numbers = set(input_tuple[110:349])
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
def return_binary_or_hexa(numbers_tuple):
    a, b = (numbers_tuple[60], numbers_tuple[90])
    missing_numbers_sum = sum(set(range(a + 1, b)).difference(numbers_tuple[60:90]))
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]
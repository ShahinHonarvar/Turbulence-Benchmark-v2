def return_binary_or_hexa(input_tuple):
    a = input_tuple[18] + 1
    b = input_tuple[60] - 1
    missing_sum = sum((x for x in range(a, b + 1) if x not in input_tuple[18:61]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
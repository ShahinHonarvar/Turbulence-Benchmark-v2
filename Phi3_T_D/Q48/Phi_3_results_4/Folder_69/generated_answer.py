def return_binary_or_hexa(input_tuple):
    a = input_tuple[39] + 1
    b = input_tuple[43] - 1
    missing_sum = sum((i for i in range(a, b + 1) if i not in input_tuple[39:43]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
def return_binary_or_hexa(number_tuple):
    a = number_tuple[18] + 1
    b = number_tuple[52] - 1
    present_numbers = set(number_tuple[18:52 + 1])
    missing_sum = sum((i for i in range(a, b + 1) if i not in present_numbers))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
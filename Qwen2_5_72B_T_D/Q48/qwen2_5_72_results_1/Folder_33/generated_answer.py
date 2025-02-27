def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    full_set = set(range(a + 1, b))
    present_set = set(numbers[14:35])
    missing_set_sum = sum(full_set - present_set)
    if missing_set_sum % 2 == 1:
        return bin(missing_set_sum)[2:]
    else:
        return hex(missing_set_sum)[2:]
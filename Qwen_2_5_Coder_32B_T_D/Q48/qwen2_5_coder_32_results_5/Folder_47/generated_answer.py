def return_binary_or_hexa(numbers):
    a, b = (numbers[29], numbers[53])
    full_set = set(range(a + 1, b))
    present_set = set(numbers[30:53])
    missing_numbers = full_set - present_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
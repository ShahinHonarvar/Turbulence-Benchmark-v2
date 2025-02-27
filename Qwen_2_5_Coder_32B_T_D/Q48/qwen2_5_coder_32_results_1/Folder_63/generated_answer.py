def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    full_set = set(range(a + 1, b))
    present_set = set(numbers[82:86])
    missing_numbers = full_set - present_set
    total_sum = sum(missing_numbers)
    if missing_numbers:
        if total_sum % 2:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
    return ''
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    full_range = set(range(a + 1, b))
    given_range = set(numbers[58:85])
    missing_numbers = full_range - given_range
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum % 2 == 0 and missing_numbers:
        return hex(total_sum)[2:]
    return ''
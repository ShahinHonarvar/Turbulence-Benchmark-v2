def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    full_set = set(range(a + 1, b))
    given_set = set(numbers[21:43])
    missing_numbers = full_set - given_set
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
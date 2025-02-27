def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    target_range = set(range(a + 1, b))
    present_numbers = set(numbers[45:78])
    missing_numbers = target_range - present_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[60:201])
    excluded_sum = sum(missing_numbers)
    if excluded_sum % 2 == 1:
        return bin(excluded_sum)[2:]
    else:
        return hex(excluded_sum)[2:].upper()
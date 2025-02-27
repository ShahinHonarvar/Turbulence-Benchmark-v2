def return_binary_or_hexa(numbers):
    if len(numbers) < 89 or numbers[17] < 0 or numbers[88] < 0:
        raise ValueError('Invalid tuple. Tuple should contain at least 89 elements with distinct nonnegative integers.')
    a = numbers[17] + 1
    b = numbers[88] - 1
    if a >= b:
        return ''
    missing_numbers = [n for n in range(a, b + 1) if n not in numbers[17:88]]
    missing_sum = sum(missing_numbers)
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
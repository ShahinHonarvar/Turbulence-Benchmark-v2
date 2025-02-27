def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200] if 200 < len(numbers) else None
    if b is None or a >= b:
        return ''
    missing_numbers_set = set(range(a + 1, b)) - set(numbers[50:200])
    missing_numbers_sum = sum(missing_numbers_set)
    if missing_numbers_sum % 2 == 1:
        return format(missing_numbers_sum, 'b')
    else:
        return format(missing_numbers_sum, 'x')
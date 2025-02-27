def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    if missing_numbers:
        total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b)).difference(numbers[86:91])
    missing_sum = sum(missing_numbers)
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x')
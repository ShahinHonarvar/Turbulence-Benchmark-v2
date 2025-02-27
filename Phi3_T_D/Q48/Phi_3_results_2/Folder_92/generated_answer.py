def return_binary_or_hexa(numbers):
    a, _, b = numbers
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:-1]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
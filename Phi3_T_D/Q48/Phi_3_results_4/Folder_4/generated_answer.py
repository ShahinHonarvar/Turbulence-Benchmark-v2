def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    if a >= b:
        return ''
    missing_set = set(range(a + 1, b)) - set(numbers[49:75])
    missing_sum = sum(missing_set)
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
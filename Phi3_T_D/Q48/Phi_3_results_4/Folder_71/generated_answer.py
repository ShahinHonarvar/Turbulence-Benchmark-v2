def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[35])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[20:35]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X')
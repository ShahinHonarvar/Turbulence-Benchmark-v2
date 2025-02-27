def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[100])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[10:100]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
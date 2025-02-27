def return_binary_or_hexa(numbers):
    a, b = (numbers[60], numbers[90])
    total_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(61, 90)))
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
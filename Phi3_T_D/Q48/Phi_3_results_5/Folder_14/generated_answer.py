def return_binary_or_hexa(numbers):
    a, b = (numbers[2], numbers[5])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[2:5]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
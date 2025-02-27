def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[20:200]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
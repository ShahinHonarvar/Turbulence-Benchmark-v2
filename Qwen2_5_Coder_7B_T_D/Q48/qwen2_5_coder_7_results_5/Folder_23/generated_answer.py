def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
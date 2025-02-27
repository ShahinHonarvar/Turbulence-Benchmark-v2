def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[20]
    b = numbers_tuple[200]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_tuple[20:200]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
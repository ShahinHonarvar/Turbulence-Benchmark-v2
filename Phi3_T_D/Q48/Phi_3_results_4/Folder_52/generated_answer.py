def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    missing_sum = sum((n for n in range(a + 1, b) if n not in numbers[38:82] and n >= a + 1))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
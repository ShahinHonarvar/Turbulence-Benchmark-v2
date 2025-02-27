def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[8])
    missing_sum = 0
    for number in range(a + 1, b):
        if number not in numbers:
            missing_sum += number
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
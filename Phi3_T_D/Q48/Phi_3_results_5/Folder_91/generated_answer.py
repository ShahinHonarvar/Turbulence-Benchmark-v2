def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[6])
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
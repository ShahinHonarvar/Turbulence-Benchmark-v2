def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[20:201]]
    actual_sum = sum(missing_numbers)
    if actual_sum % 2 == 0:
        return format(actual_sum, 'x')
    else:
        return format(actual_sum, 'b')
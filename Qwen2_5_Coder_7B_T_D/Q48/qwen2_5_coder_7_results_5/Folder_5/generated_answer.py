def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            total_sum += num
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
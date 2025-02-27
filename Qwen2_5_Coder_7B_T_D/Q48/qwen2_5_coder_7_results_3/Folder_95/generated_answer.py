def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[33:100]]
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
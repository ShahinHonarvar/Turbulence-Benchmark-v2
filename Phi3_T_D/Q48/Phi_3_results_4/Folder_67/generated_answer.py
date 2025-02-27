def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    missing_numbers_set = set(range(a + 1, b))
    for index in range(44, 67 + 1):
        if a < numbers[index] < b:
            missing_numbers_set.discard(numbers[index])
    total_sum = sum(missing_numbers_set)
    if total_sum % 2 == 0:
        return hex(total_sum)
    else:
        return format(total_sum, 'b')
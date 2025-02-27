def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[934:996])
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 0:
        return format(sum_of_missing, 'x')
    else:
        return format(sum_of_missing, 'b')
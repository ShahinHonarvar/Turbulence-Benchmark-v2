def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[55:85])
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 0:
        return format(sum_of_missing, 'x')
    else:
        return format(sum_of_missing, 'b')
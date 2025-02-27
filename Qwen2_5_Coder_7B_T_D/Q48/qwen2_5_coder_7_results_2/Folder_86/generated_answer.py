def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return format(sum_missing, 'X')
    else:
        return bin(sum_missing)[2:]
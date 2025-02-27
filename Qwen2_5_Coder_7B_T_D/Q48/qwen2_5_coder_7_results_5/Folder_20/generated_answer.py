def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]
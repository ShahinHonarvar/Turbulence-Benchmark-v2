def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[9])
    complete_range = set(range(a + 1, b))
    missing_numbers = list(complete_range - set(numbers))
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
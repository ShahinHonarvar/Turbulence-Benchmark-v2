def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    range_set = set(range(a + 1, b))
    present_numbers = set(numbers[18:88])
    missing_numbers = range_set - present_numbers
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
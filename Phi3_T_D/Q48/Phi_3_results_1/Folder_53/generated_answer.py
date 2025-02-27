def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    all_numbers = set(range(a + 1, b))
    tuple_slice = set(numbers[200:203])
    missing_numbers = all_numbers - tuple_slice
    total_missing = sum(missing_numbers)
    if total_missing % 2 == 0:
        return hex(total_missing)[2:]
    else:
        return bin(total_missing)[2:]
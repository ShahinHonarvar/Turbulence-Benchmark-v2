def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    total_sum = sum(range(a + 1, b))
    missing_integers = [i for i in range(a + 1, b) if i not in numbers[44:79]]
    sum_of_missing = sum(missing_integers)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()
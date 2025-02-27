def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[33:44]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
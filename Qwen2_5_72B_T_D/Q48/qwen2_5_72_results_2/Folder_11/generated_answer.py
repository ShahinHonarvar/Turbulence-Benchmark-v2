def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[49:76]))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
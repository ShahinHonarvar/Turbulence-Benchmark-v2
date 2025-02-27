def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[57:90]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
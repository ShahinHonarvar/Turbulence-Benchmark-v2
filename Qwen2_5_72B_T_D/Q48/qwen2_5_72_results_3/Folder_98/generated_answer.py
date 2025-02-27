def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[78:84]))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
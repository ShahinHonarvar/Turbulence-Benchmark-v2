def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[21:35]))
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
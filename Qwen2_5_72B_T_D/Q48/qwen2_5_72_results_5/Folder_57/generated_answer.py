def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[26:80]))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
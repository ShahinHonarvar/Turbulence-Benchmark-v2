def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    sum_excluded = sum(set(range(a + 1, b)).difference(numbers[27:97]))
    if sum_excluded % 2 == 0:
        return hex(sum_excluded)[2:]
    else:
        return bin(sum_excluded)[2:]
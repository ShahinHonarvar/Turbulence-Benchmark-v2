def return_binary_or_hexa(numbers):
    if len(numbers) < 65:
        return None
    a = numbers[35]
    b = numbers[64]
    sum_excluded = sum((x for x in range(a + 1, b) if x not in numbers[35:65]))
    if sum_excluded % 2 != 0:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]
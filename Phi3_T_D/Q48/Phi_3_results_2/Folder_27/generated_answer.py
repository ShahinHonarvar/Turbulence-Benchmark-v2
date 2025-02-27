def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    included = set(numbers[86:90])
    sum_excluded = sum((i for i in range(a + 1, b) if i not in included))
    if sum_excluded % 2 == 0:
        return hex(sum_excluded).lstrip('0x').upper()
    else:
        return bin(sum_excluded)[2:]
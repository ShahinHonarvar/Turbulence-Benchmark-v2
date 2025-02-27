def return_binary_or_hexa(numbers: tuple) -> str:
    a, b = (numbers[29], numbers[53])
    sum_of_missing = sum((x for x in range(a + 1, b) if x not in numbers[29:54]))
    if sum_of_missing % 2 == 1:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')
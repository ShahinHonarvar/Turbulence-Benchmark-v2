def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers))
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')
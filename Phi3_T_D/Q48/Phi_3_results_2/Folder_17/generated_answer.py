def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[73:85]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return '{0:b}'.format(missing_sum)[2:]
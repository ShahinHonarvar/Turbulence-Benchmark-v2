def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    absent_sum = sum((x for x in range(a + 1, b) if x not in numbers[17:89]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return '{0:b}'.format(absent_sum)
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x').upper()
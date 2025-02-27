def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    missing_sum = sum([i for i in range(a + 1, b) if i not in numbers[10:80]])
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')
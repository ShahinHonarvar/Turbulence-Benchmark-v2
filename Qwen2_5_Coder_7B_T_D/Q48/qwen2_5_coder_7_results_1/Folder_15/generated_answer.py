def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    total_sum = sum(range(a + 1, b)) - sum(numbers[1:4])
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')
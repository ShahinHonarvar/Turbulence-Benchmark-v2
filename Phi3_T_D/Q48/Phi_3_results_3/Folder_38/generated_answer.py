def return_binary_or_hexa(numbers):
    a, b = (numbers[36], numbers[85])
    available_sum = sum(range(a + 1, b)) - sum(numbers[36:85 + 1])
    if available_sum % 2 == 0:
        return '{:X}'.format(abs(available_sum))
    else:
        return '{0:b}'.format(abs(available_sum))[::-1]
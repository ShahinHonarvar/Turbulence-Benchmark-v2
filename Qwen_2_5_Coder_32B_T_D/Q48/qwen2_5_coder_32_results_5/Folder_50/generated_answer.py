def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for i, x in enumerate(numbers) if 13 < i < 76 and a + 1 <= x < b))
    difference = expected_sum - actual_sum
    if difference == 0:
        return ''
    elif difference % 2 == 1:
        return bin(difference)[2:]
    else:
        return hex(difference)[2:]
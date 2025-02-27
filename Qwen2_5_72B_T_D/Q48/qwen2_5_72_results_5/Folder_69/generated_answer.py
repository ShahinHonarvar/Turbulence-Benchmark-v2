def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    present_numbers = set(numbers[40:43])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
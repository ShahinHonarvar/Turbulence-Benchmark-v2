def return_binary_or_hexa(numbers):
    if len(numbers) < 68:
        return ''
    a = numbers[44]
    b = numbers[67]
    present_numbers = set(numbers[45:67])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
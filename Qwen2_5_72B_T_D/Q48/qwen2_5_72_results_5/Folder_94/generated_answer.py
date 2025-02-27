def return_binary_or_hexa(numbers):
    if len(numbers) < 88:
        return ''
    a, b = (numbers[42], numbers[87])
    if a + 1 >= b:
        return ''
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[43:87]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
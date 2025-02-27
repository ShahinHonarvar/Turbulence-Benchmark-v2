def return_binary_or_hexa(numbers):
    if len(numbers) < 70:
        return ''
    a = numbers[34]
    b = numbers[69]
    if a + 1 >= b:
        return ''
    present_numbers = set(numbers[35:69])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
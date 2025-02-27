def return_binary_or_hexa(numbers):
    if len(numbers) < 36 or numbers[13] + 1 >= numbers[35] - 1:
        return ''
    a, b = (numbers[13], numbers[35])
    existing_numbers = set(numbers[14:35])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
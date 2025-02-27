def return_binary_or_hexa(numbers):
    if not 2 <= len(numbers) <= 8:
        return ''
    a, b = (numbers[2], numbers[8])
    all_numbers = set(range(a + 1, b))
    given_numbers = set(numbers[2:9])
    missing_numbers = all_numbers - given_numbers
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
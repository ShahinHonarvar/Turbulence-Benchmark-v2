def return_binary_or_hexa(numbers):
    a, _, _, _, b = numbers
    all_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[1:5])
    missing_numbers = all_numbers - present_numbers
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 1:
        return f'{bin(missing_sum)[2:]}'
    else:
        return f'{hex(missing_sum)[2:]}'
def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    existing_numbers = set(numbers[19:52])
    missing_sum = sum(set(range(a + 1, b)) - existing_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
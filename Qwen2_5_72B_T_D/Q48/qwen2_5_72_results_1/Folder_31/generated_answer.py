def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    existing_numbers = set(numbers[34:78])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
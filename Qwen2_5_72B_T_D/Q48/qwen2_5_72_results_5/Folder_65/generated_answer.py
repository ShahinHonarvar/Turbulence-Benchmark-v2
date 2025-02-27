def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    existing_numbers = set(numbers[52:76])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
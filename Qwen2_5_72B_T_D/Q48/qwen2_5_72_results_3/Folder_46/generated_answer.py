def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    existing_numbers = set(numbers[10:80])
    missing_sum = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
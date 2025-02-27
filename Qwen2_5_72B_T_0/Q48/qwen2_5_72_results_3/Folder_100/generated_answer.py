def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    present_numbers = set(numbers[45:78])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
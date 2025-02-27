def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[40:201]]
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
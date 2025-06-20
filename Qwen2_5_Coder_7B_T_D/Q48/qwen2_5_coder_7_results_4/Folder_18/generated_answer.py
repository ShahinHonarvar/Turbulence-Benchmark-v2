def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[a + 1:b]]
    if missing_numbers:
        total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[50:201]]
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
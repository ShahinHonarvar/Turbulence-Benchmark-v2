def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[60:201]]
    if sum(missing_numbers) % 2 == 1:
        return bin(sum(missing_numbers))[2:]
    else:
        return hex(sum(missing_numbers))[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[450:906])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
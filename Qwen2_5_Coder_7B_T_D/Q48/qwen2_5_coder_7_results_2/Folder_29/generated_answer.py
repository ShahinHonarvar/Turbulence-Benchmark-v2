def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[70:99]]
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
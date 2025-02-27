def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    total_sum = sum(range(a + 1, b))
    numbers_set = set(numbers)
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_set))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
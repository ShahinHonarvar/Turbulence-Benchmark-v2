def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
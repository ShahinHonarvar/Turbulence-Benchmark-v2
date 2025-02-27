def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[20:200]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper() if missing_sum != 0 else ''
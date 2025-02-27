def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[73:85]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:] if missing_sum else ''
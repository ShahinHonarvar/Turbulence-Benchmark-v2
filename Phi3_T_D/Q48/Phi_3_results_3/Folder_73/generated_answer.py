def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[10:76 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    total_sum = sum(range(a + 1, b))
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[36:53]))
    if total_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
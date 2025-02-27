def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[86:90]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
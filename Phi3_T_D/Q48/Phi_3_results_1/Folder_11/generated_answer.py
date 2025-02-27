def return_binary_or_hexa(numbers):
    if len(numbers) < 77:
        return ''
    a = numbers[48]
    b = numbers[76]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[48:77]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    if a + 1 >= b - 1:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    if len(numbers) < 44:
        return ''
    a = numbers[37]
    b = numbers[43]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
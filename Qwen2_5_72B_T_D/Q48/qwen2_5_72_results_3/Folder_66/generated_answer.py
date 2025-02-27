def return_binary_or_hexa(numbers):
    if len(numbers) < 77 or numbers[11] + 1 >= numbers[76] - 1:
        return ''
    a = numbers[11]
    b = numbers[76]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
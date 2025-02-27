def return_binary_or_hexa(numbers):
    if len(numbers) < 9:
        return ''
    a = numbers[2]
    b = numbers[8]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            missing_sum += num
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
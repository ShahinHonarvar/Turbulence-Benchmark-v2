def return_binary_or_hexa(numbers):
    if len(numbers) < 349 or len(numbers) < 111:
        return ''
    a = numbers[110]
    b = numbers[348]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[111:348]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
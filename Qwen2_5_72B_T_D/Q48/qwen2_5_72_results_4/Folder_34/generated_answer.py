def return_binary_or_hexa(numbers):
    if len(numbers) <= 200 or len(numbers) < 61:
        return ''
    a = numbers[60]
    b = numbers[200]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[61:200]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
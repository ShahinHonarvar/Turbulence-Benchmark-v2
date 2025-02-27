def return_binary_or_hexa(numbers):
    if len(numbers) < 77 or numbers[13] + 1 >= numbers[76]:
        return ''
    a = numbers[13]
    b = numbers[76]
    missing_sum = sum(range(a + 1, b))
    for num in numbers[14:76]:
        if a + 1 <= num <= b - 1:
            missing_sum -= num
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
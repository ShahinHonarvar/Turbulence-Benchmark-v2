def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    total_sum = 0
    present_numbers = set(numbers[19:60])
    for i in range(a + 1, b):
        if i not in present_numbers:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    return ''
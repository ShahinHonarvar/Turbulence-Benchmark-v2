def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    elif missing_sum:
        return hex(missing_sum)[2:]
    return ''
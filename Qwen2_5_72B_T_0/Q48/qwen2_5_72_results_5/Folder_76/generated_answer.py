def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
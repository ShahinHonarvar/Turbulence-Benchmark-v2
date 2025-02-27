def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[11:77]:
            missing_sum += num
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
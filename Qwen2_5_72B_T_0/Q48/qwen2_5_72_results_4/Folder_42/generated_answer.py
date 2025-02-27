def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    present_numbers = set(numbers[19:60])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
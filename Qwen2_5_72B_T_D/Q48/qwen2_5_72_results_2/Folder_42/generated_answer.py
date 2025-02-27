def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    present_set = set(numbers[19:60])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_set))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
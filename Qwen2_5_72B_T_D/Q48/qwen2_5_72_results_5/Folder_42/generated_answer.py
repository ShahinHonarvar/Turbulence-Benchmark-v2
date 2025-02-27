def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[19:60]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[38:43]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
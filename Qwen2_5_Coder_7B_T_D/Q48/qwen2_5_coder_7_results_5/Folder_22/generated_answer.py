def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    total_sum = sum(range(a + 1, b))
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[40:201]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a, b = (numbers[17], numbers[88])
    missing_sum = sum(range(a + 1, b)) - sum(numbers[17:88])
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
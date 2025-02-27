def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[58:85]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[57:86]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[71:98]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
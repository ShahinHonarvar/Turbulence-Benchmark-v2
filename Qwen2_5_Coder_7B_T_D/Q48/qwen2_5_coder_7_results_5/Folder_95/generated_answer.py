def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    missing_sum = sum(range(a + 1, b)) - sum(set(numbers[32:100]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
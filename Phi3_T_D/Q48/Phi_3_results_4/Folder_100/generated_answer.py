def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[44:79]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
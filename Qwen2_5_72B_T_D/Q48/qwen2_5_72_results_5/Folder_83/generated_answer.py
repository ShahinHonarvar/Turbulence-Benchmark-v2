def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[91:200]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
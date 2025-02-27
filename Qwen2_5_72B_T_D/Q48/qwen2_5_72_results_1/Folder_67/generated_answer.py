def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[45:67]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[91:97]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
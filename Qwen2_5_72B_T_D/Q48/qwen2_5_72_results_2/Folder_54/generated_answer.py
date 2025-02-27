def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[36:64]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
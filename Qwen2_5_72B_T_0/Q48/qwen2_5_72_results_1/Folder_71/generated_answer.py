def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[21:35]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
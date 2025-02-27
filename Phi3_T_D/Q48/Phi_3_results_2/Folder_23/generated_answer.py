def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    missing_sum = sum(range(a + 1, b)) - sum(numbers[20 + 1:36])
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
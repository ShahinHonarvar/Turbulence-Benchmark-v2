def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    missing_sum = sum(range(a + 1, b)) - sum(numbers[42 + 1:87])
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
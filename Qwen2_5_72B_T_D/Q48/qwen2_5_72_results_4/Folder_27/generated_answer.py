def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[87:89]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    total_sum = sum(set(range(a + 1, b)) - set(numbers[33:44]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
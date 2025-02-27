def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    total_sum = sum(range(a + 1, b)) - sum(set(numbers[35:69]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
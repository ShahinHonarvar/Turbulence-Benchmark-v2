def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    return_values = set(range(a + 1, b)) - set(numbers[427:669 + 1])
    total_sum = sum(return_values)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
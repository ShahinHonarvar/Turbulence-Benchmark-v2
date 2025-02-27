def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[86:91])
    total_sum -= sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
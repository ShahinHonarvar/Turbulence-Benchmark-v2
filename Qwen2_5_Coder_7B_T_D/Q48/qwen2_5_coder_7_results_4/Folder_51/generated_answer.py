def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[7:9])
    total_sum -= sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
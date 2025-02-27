def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[69:98])
    if missing_numbers:
        total_sum += sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
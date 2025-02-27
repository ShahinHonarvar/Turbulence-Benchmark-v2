def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[20:36]]
    for num in missing_numbers:
        total_sum -= num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
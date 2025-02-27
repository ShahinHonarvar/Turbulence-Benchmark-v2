def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[10:98]]
    if missing_numbers:
        total_sum -= sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
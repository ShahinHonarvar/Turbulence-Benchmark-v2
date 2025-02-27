def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[a + 1:b]]
    if missing_numbers:
        total_sum += sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[55:85]]
    if missing_numbers:
        missing_sum = sum(missing_numbers)
        if missing_sum % 2 == 1:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:]
    else:
        return ''
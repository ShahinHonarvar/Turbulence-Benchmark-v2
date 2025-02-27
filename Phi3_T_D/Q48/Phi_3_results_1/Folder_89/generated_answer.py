def return_binary_or_hexa(numbers):
    a = numbers[55] if len(numbers) > 55 else None
    b = numbers[84] if len(numbers) > 84 else None
    if a and b and (a < b):
        missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[55:85]))
        sum_type = bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
        return sum_type.upper() if sum_type[0].isdigit() else sum_type
    return ''
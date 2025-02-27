def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    present_set = set(numbers[20:37])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_set))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b').lstrip('0b')
    else:
        return format(missing_sum, 'x').lstrip('0x').lower()
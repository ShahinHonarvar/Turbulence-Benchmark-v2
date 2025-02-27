def return_binary_or_hexa(numbers):
    if len(numbers) < 85:
        return ''
    a = numbers[73]
    b = numbers[84]
    if a + 1 >= b:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
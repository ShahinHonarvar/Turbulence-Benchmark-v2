def return_binary_or_hexa(numbers):
    if len(numbers) < 89 or numbers[56] + 1 >= numbers[88]:
        return ''
    a = numbers[56]
    b = numbers[88]
    existing_numbers = set(numbers[57:88])
    missing_sum = sum(set(range(a + 1, b)) - existing_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
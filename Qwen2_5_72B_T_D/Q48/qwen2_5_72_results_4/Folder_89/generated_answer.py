def return_binary_or_hexa(numbers):
    if len(numbers) < 85:
        return ''
    a = numbers[55]
    b = numbers[84]
    subset = set(numbers[56:84])
    missing_sum = sum(set(range(a + 1, b)) - subset)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
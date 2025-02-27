def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    present_numbers = set(numbers[74:84])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
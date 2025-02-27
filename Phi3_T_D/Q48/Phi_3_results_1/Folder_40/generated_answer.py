def return_binary_or_hexa(numbers):
    a, _, _, b = numbers
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[1:b]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    present_numbers = set(numbers[14:35])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
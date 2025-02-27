def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    present = set(numbers[37:44])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
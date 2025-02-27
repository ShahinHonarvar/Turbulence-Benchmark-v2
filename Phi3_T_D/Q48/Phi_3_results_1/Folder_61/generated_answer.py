def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[8])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
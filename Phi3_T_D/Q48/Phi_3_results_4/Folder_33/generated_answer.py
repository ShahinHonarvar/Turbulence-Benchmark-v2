def return_binary_or_hexa(numbers):
    a, b = (numbers[13], numbers[35])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[13:35]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
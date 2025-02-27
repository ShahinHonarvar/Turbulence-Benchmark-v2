def return_binary_or_hexa(numbers):
    a, b = (numbers[6], numbers[7])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[6:7]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
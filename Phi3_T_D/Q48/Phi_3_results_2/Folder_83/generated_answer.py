def return_binary_or_hexa(numbers):
    a, b = (numbers[90], numbers[200])
    missing_sum = sum(range(a + 1, b), key=lambda x: x not in numbers[90:201])
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
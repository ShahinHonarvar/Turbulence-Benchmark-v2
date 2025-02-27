def return_binary_or_hexa(numbers):
    a, b = (numbers[40], numbers[200])
    missing_sum = sum((n for n in range(a + 1, b) if n not in numbers[40:200]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
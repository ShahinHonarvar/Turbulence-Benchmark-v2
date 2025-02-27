def return_binary_or_hexa(numbers):
    start, end = (275, 871)
    missing_sum = sum((n for n in range(numbers[start] + 1, numbers[end]) if n not in numbers[start:end + 1]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
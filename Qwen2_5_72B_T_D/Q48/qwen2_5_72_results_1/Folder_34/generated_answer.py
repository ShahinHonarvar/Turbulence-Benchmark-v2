def return_binary_or_hexa(numbers):
    a, b = (numbers[60], numbers[200])
    numbers_set = set(numbers[61:200])
    missing_sum = sum((num for num in range(a + 1, b) if num not in numbers_set))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
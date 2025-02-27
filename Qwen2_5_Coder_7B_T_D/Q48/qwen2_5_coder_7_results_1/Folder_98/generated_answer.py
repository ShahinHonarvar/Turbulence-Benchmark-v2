def return_binary_or_hexa(numbers):
    a, b = (numbers[6], numbers[7])
    missing_sum = sum(range(a + 1, b)) - sum((num for num in numbers if a < num < b))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
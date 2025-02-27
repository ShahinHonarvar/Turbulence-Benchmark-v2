def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[4])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((num for num in range(a + 1, b) if num not in numbers))
    if actual_sum % 2 == 1:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    present_numbers = set(numbers[34:78])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    present_numbers = set(numbers[35:65])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
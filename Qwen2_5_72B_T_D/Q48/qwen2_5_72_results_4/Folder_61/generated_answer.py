def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    present_numbers = set(numbers[1:8])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
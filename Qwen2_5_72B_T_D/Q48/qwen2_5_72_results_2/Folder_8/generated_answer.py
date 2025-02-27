def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    missing_sum = sum((num for num in range(a + 1, b) if num not in numbers[46:48]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
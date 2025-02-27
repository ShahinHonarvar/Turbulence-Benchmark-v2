def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[7]
    present_numbers = set(numbers[numbers.index(a) + 1:numbers.index(b)])
    missing_sum = sum(set(range(a + 1, b)) - present_numbers)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
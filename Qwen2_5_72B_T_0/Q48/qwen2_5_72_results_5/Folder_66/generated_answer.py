def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    present_numbers = set(numbers[11:77])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
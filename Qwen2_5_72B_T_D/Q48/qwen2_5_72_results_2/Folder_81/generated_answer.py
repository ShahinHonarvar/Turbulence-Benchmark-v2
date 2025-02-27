def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[100]
    present_numbers = set(numbers[10:101])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
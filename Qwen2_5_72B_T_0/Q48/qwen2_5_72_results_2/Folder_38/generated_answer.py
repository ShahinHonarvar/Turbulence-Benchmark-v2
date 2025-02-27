def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    present_numbers = set(numbers[37:85])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
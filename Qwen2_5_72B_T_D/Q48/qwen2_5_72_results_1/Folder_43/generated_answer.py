def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    present_nums = set(numbers[11:28])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
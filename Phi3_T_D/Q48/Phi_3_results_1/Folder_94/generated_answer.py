def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    present_nums = set(numbers[a + 1:b])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
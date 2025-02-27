def return_binary_or_hexa(numbers):
    a, b = (numbers[15], numbers[57])
    existing_nums = set(numbers[15:58])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_nums))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
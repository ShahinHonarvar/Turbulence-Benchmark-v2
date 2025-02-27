def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    present = set(numbers[16:57])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
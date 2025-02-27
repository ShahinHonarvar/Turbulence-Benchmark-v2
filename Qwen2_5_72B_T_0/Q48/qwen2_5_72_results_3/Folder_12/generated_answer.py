def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    present = set(numbers[17:87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    present = set(numbers[81:87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]
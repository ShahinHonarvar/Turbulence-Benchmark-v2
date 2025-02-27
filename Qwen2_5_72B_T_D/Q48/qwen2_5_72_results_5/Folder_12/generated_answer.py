def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    present = set(numbers[17:87])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
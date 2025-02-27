def return_binary_or_hexa(numbers):
    a, b = (numbers[48], numbers[76])
    present = set(numbers[48:77])
    total = sum((x for x in range(a + 1, b) if x not in present))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
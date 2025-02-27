def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    present = set(numbers[39:52])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
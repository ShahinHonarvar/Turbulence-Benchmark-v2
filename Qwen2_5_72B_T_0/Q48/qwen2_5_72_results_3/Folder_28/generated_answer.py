def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    present = set(numbers[86:100])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
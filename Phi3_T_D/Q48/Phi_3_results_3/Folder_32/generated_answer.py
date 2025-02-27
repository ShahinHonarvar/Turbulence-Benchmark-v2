def return_binary_or_hexa(numbers):
    a, b = (numbers[86], numbers[90])
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[86:90]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
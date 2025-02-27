def return_binary_or_hexa(numbers):
    a, b = (numbers[68], numbers[99])
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[68:99 + 1]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
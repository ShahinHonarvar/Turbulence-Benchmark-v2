def return_binary_or_hexa(numbers):
    a, _, _, _, b = numbers
    missing_sum = sum(set(range(a + 1, b)).difference(numbers))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
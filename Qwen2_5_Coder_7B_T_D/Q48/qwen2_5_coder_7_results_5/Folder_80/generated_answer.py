def return_binary_or_hexa(numbers):
    a, b = (numbers[57], numbers[84])
    missing_sum = sum(range(a + 1, b)) - sum(set(numbers[57:85]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
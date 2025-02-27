def return_binary_or_hexa(numbers):
    a, b = (numbers[38], numbers[81])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[39:81]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
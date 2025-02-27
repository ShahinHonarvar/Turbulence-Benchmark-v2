def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[62:97]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
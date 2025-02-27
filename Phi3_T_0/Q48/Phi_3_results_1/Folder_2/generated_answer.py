def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[72:94]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
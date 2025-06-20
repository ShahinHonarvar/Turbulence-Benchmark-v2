def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[10:13]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
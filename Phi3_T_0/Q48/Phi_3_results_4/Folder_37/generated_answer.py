def return_binary_or_hexa(numbers):
    a, b = (numbers[2], numbers[7])
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[2:8]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
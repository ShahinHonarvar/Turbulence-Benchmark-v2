def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[10])
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[1:11]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
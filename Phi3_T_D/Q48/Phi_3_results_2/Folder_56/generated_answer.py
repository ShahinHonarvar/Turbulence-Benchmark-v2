def return_binary_or_hexa(numbers):
    a, b = (numbers[7], numbers[9])
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[7:10]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
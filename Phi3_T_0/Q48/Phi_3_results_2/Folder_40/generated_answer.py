def return_binary_or_hexa(numbers):
    a, _, _, b = numbers
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[1:3]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
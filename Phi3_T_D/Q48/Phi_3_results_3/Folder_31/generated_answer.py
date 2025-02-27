def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[33:79]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
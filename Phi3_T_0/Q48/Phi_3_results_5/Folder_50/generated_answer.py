def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[13:77]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
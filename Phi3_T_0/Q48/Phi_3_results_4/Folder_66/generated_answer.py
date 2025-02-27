def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[11:77]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
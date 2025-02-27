def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    missing_integers_sum = sum(range(a + 1, b)) - sum(numbers[10 + 1:28])
    if missing_integers_sum % 2 != 0:
        return bin(missing_integers_sum)[2:]
    else:
        return hex(missing_integers_sum)[2:].upper()
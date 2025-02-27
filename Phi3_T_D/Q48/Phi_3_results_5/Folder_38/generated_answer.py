def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    absent_sum = sum(set(range(a + 1, b)) - set(numbers[36:85]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:].upper()
    else:
        return bin(absent_sum)[2:]
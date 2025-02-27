def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a + 1 <= x <= b - 1, numbers[51:77]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
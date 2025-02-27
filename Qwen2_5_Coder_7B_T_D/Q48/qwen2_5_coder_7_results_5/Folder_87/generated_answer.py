def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a + 1 <= x <= b - 1, numbers[20:44]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
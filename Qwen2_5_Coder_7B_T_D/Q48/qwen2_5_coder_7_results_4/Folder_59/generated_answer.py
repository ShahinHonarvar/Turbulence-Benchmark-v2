def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    total_sum = sum(range(a + 1, b)) - sum((x for x in numbers if a + 1 <= x <= b - 1))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    total_sum = sum(range(a + 1, b)) - sum((n for n in numbers if a + 1 <= n <= b - 1))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
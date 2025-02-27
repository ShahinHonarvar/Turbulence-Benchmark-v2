def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    target_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(70, 99)))
    if target_sum % 2 == 1:
        return bin(target_sum)[2:]
    else:
        return hex(target_sum)[2:].upper()
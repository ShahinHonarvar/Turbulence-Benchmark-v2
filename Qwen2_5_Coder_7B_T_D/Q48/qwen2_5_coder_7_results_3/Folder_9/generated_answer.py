def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    total_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(70, 201)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
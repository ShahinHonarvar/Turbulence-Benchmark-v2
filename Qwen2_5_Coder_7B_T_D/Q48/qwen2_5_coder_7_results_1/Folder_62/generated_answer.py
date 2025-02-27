def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total = sum(range(a + 1, b)) - sum((numbers[i] for i in range(50, 93)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[2])
    total_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(3, len(numbers))))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
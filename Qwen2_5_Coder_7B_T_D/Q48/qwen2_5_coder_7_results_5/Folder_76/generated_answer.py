def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    total_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(451, 905)))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
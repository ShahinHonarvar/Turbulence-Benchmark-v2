def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    total_sum = sum(range(a + 1, b)) - sum((numbers[i] for i in range(21, 35)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
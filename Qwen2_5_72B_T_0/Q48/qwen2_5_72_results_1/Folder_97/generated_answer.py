def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    present = set(numbers[35:69])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
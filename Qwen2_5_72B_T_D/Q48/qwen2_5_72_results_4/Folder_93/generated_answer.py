def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    subset = set(numbers[58:85])
    total_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
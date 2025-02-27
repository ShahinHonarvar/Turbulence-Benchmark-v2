def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    subset = set(numbers[18:88])
    total = sum((i for i in range(a + 1, b) if i not in subset))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    present = set(numbers[18:88])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
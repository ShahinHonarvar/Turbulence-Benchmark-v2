def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    total_sum = sum(range(a + 1, b))
    present_numbers = set(numbers[a + 1:b])
    for i in range(a + 1, b):
        if i in present_numbers:
            total_sum -= i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
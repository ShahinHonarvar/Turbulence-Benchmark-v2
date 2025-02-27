def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    total_sum = sum(range(a + 1, b))
    absent_numbers = set(range(a + 1, b)) - set(numbers[a + 1:b])
    for num in absent_numbers:
        total_sum += num
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
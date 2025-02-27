def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    total_sum = sum(range(a + 1, b)) - sum(set(numbers[a + 1:b]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
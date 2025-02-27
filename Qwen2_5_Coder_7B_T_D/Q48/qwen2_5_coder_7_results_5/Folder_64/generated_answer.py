def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[5])
    total_sum = sum(range(a + 1, b)) - sum(set(numbers[1:5]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
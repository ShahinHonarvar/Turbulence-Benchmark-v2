def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[3])
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
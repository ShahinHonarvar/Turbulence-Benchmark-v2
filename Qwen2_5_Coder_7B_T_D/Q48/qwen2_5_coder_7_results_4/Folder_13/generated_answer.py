def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[46:92]]
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
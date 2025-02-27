def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    required_sum = sum(range(a + 1, b)) - sum(numbers[a + 1:b])
    if required_sum % 2 == 1:
        return bin(required_sum)[2:]
    else:
        return hex(required_sum)[2:].upper()
def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    required_sum = sum(range(a + 1, b)) - sum((number for number in numbers if a < number < b))
    if required_sum % 2 == 1:
        return bin(required_sum)[2:]
    else:
        return hex(required_sum)[2:].upper()
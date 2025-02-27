def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: x > a and x < b, numbers))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
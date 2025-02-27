def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a < x < b, numbers[90:201]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
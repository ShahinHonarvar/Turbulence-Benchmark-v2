def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a < x < b, numbers[27:97]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
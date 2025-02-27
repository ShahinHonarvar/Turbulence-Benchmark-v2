def return_binary_or_hexa(numbers):
    a, b = (numbers[6], numbers[7])
    range_sum = (b - a) * (a + b) // 2 - sum(numbers[6:7])
    if range_sum == 0:
        return ''
    if range_sum % 2 != 0:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
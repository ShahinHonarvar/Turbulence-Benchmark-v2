def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers[52:76]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
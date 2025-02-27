def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    not_in_range = set(range(a + 1, b)) - set(numbers[13:92])
    if not not_in_range:
        return ''
    total = sum(not_in_range)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
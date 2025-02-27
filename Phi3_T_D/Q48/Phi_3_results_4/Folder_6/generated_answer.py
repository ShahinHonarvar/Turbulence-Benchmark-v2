def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[93])
    total = sum(set(range(a + 1, b)) - set(numbers[20:93 + 1]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
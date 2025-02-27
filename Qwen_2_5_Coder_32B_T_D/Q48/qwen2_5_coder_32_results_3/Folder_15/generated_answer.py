def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[4])
    total = 0
    present = set(numbers[:5])
    for i in range(a + 1, b):
        if i not in present:
            total += i
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    present = set(numbers[44:70])
    total = 0
    for num in range(a + 1, b):
        if num not in present:
            total += num
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
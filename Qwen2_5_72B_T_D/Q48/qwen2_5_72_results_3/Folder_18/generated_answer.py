def return_binary_or_hexa(data):
    a = data[56]
    b = data[90]
    available = set(data[57:90])
    total = 0
    for number in range(a + 1, b):
        if number not in available:
            total += number
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
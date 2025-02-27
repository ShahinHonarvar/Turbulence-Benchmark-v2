def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    total = sum((x for x in range(a + 1, b) if x not in numbers[87:99]))
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in numbers[20:200]]
    if total == sum(missing):
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
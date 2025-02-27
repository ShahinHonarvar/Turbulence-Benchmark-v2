def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[57:86]:
            missing_sum += i
    if missing_sum % 2 == 0:
        hexa = hex(missing_sum)[2:]
    else:
        binary = bin(missing_sum)[2:]
    if missing_sum == 0:
        return ''
    else:
        return hexa if hexa else binary
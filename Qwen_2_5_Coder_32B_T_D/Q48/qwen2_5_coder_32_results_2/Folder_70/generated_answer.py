def return_binary_or_hexa(numbers):
    a, b = (numbers[43], numbers[70])
    if a + 1 >= b - 1:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[43:71]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
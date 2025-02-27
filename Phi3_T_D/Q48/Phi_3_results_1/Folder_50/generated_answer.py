def return_binary_or_hexa(numbers):
    try:
        a = numbers[13]
        b = numbers[76]
    except IndexError:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[13:77]))
    missing_sum += b if b not in numbers[13:77] else 0
    return bin(missing_sum)[2:] if missing_sum % 2 else format(missing_sum, 'x')
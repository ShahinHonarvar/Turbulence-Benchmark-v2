def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    missing = [n for n in range(a + 1, b) if n not in numbers[80:200]]
    missing_sum = sum(missing)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)
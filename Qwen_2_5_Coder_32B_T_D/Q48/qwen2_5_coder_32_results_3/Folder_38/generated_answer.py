def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    full_range = set(range(a + 1, b))
    given_range = set(numbers[37:85])
    missing_numbers = full_range - given_range
    if not missing_numbers:
        return ''
    s = sum(missing_numbers)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]
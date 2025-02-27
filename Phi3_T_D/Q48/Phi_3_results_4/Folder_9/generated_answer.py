def return_binary_or_hexa(numbers_tuple):
    if not 70 < len(numbers_tuple) <= 200:
        return ''
    a = numbers_tuple[70]
    b = numbers_tuple[200]
    numbers_set = set(numbers_tuple)
    valid_numbers = [i for i in range(a + 1, b) if i not in numbers_set]
    if not valid_numbers:
        return ''
    sum_valid_numbers = sum(valid_numbers)
    if sum_valid_numbers % 2 == 0:
        return f'{sum_valid_numbers:x}'
    else:
        return f'{bin(sum_valid_numbers)[2:]}'
def return_binary_or_hexa(number_tuple):
    if not 110 < len(number_tuple) > 348:
        return ''
    a_index, b_index = (110, 348)
    sum_numbers = sum(set(range(number_tuple[a_index] + 1, number_tuple[b_index])) - set(number_tuple[a_index:b_index]))
    if sum_numbers == 0:
        return ''
    elif sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    return bin(sum_numbers)[2:]
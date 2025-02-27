def return_binary_or_hexa(input_tuple):
    a, _, _, _, _, _, _, _, _, _, b = input_tuple
    total_sum = sum((x for x in range(a + 1, b) if x not in input_tuple))
    if total_sum % 2 == 0:
        return f'{total_sum:#x}'
    else:
        return f'{total_sum:b}'
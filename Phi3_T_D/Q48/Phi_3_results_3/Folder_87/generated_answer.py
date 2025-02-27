def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[43]
    sum_value = sum(set(range(a + 1, b)) - set((input_tuple[s] for s in range(20, 44))))
    if not sum_value:
        return ''
    return bin(sum_value)[2:] if sum_value % 2 else hex(sum_value)[2:].upper()
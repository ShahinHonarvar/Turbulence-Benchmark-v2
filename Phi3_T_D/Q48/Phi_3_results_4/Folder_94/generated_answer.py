def return_binary_or_hexa(int_tuple):
    missing_sum = sum(set(range(int_tuple[42] + 1, int_tuple[87])) - set(int_tuple[42:88]))
    if missing_sum % 2 == 0:
        return f'{missing_sum:#x}'
    else:
        return f'{missing_sum:#b}'
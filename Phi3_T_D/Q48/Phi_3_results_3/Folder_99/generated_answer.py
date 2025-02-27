def return_binary_or_hexa(num_tuple):
    a = num_tuple[427]
    b = num_tuple[669]
    missing_sum = sum(set(range(a + 1, b)) - set(num_tuple[427:669 + 1]))
    if missing_sum % 2 != 0:
        return f'{bin(missing_sum)[2:]}'
    else:
        return f'{hex(missing_sum)[2:]}'
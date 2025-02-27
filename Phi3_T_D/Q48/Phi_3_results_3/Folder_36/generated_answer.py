def return_binary_or_hexa(n_tuple):
    missing_sum = 0
    for num in range(n_tuple[110] + 1, n_tuple[348]):
        if num not in n_tuple[n_tuple[110]:n_tuple[348]]:
            missing_sum += num
    if missing_sum % 2 != 0:
        return f'{bin(missing_sum)[2:]}'
    else:
        return f'{hex(missing_sum)[2:]}'
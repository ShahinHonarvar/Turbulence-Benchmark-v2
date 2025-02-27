def return_binary_or_hexa(tpl):
    a, b = (tpl[49], tpl[74])
    missing_sum = sum((x for x in range(a + 1, b) if x not in tpl[49:75]))
    if missing_sum % 2 == 1:
        return f'{bin(missing_sum)[2:]}'
    return f'{hex(missing_sum)[2:]}'
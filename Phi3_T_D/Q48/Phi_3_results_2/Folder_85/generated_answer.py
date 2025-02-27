def return_binary_or_hexa(tpl):
    a, _, _, _, _, _, _, _, _, _, b = tpl
    missing_sum = sum(set(range(a + 1, b)).difference(tpl[1:8]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return format(missing_sum, 'b')
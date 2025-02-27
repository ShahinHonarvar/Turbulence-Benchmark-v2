def return_binary_or_hexa(tupl):
    a = tupl[38]
    b = tupl[52]
    missing_sum = sum(set(range(a + 1, b)) - set(tupl[38:53]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return f'{missing_sum:b}'
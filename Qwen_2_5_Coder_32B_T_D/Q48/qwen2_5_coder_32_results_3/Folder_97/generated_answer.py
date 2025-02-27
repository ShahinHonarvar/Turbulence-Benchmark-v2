def return_binary_or_hexa(tpl):
    a = tpl[34]
    b = tpl[69]
    full_set = set(range(a + 1, b))
    tpl_set = set(tpl[35:69])
    diff_set = full_set - tpl_set
    total_sum = sum(diff_set)
    if not diff_set:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
def return_binary_or_hexa(tpl):
    a = tpl[86]
    b = tpl[89]
    sum_ab = sum(range(a + 1, b))
    missing_sum = sum_ab - sum(tpl[a + 1:b])
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')
def return_binary_or_hexa(tpl):
    a, b = (tpl[0], tpl[8])
    sum_absent = sum((i for i in range(a + 1, b) if i not in tpl[:9]))
    return bin(sum_absent)[2:] if sum_absent % 2 else hex(sum_absent)[2:]
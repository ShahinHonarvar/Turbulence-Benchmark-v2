def return_binary_or_hexa(tpl):
    a, b = (tpl[13], tpl[76])
    subset_sum = sum((i for i in range(a + 1, b) if i not in tpl[13:77]))
    if subset_sum % 2 == 0:
        return hex(subset_sum)[2:]
    else:
        return bin(subset_sum)[2:]
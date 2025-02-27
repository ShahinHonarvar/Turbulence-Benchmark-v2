def return_binary_or_hexa(tpl):
    a = tpl[32]
    b = tpl[44]
    missing_sum = sum(set(range(a + 1, b)) - set(tpl[33:44]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
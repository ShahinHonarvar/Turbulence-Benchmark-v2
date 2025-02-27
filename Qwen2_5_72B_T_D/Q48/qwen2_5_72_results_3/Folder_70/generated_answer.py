def return_binary_or_hexa(tpl):
    a = tpl[43]
    b = tpl[70]
    missing_sum = sum(set(range(a + 1, b)) - set(tpl[44:70]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
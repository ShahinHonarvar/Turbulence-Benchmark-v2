def return_binary_or_hexa(tpl):
    if not tpl or 450 >= len(tpl) or 905 >= len(tpl):
        return ''
    a = tpl[450]
    b = tpl[905]
    included_values = set(tpl[450:906])
    values_to_sum = [i for i in range(a + 1, b) if i not in included_values]
    total_sum = sum(values_to_sum)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
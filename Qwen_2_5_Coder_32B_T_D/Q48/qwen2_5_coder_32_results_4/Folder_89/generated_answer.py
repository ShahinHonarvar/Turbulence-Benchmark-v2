def return_binary_or_hexa(tpl):
    a = tpl[55]
    b = tpl[84]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in tpl[56:84]:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
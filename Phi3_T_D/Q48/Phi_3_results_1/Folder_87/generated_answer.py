def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[20:44]))
    return_format = bin if missing_sum % 2 else hex
    return '' if a >= b or missing_sum == 0 else return_format(missing_sum).lstrip('0xob')
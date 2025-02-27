def return_binary_or_hexa(t):
    a = t[51] + 1
    b = t[76]
    if a >= b - 1:
        return ''
    missing_ints = set(range(a, b)).difference(set(t[51:77]))
    missing_sum = sum(missing_ints)
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
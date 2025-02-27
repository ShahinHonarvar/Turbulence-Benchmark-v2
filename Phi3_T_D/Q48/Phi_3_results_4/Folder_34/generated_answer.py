def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    missing_sum = sum(set(range(a + 1, b)) - set(t[60 + 1:200 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return '{0:b}'.format(missing_sum)[2:]
def return_binary_or_hexa(t):
    a, b = (t[51], t[76])
    missing_sum = sum(set(range(a + 1, b)).difference(set(t[51:77])))
    return bin(missing_sum)[2:] if missing_sum % 2 else format(missing_sum, 'x')
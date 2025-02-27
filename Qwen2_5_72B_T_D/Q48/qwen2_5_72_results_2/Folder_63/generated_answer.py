def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    missing_sum = sum(set(range(a + 1, b)) - set(t[82:86]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
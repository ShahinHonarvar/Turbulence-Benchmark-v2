def return_binary_or_hexa(t):
    range_elems = set(t[57:86])
    a, b = (t[57], t[85])
    missing_sum = sum((x for x in range(a + 1, b) if x not in range_elems))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
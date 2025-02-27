def return_binary_or_hexa(seq):
    a, b = (seq[81], seq[86])
    missing_sum = sum((x for x in range(a + 1, b) if x not in seq[81:86]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
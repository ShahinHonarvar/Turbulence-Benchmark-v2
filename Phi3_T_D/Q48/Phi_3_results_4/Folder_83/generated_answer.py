def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    missing_sum = sum(set(range(a + 1, b)) - set(t[90:201]))
    if missing_sum % 2:
        return str(bin(missing_sum))[2:]
    return hex(missing_sum)[2:].upper()
def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    missing_sum = sum(range(a + 1, b)) - sum((t[i] for i in range(27, 97)))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
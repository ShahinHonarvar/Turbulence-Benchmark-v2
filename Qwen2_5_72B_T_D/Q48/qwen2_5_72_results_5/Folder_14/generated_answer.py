def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    missing_sum = sum(set(range(a + 1, b)) - set(t[3:5]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
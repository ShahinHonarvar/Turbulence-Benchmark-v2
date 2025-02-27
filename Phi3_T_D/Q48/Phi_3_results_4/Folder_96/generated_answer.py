def return_binary_or_hexa(t):
    a = t[50]
    b = t[200]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[50:201]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
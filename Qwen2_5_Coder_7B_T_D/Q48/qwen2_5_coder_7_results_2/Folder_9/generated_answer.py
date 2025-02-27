def return_binary_or_hexa(t):
    a, b = (t[70], t[200])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[70:201]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
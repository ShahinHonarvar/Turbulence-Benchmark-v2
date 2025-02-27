def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[934:996]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
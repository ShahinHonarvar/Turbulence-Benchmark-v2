def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    present = set(t[87:90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
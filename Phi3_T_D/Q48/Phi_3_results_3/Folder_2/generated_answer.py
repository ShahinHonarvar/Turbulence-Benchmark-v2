def return_binary_or_hexa(t):
    a = t[71]
    b = t[92]
    missing_sum = sum(set(range(a + 1, b)) - set(t[71:92]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]
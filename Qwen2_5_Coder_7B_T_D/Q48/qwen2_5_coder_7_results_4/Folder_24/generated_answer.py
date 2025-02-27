def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    total_sum = sum(range(a + 1, b)) - sum((i for i in range(a + 1, b) if i in t[13:92]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    total_sum = sum(range(a + 1, b)) - sum((t[i] for i in range(35, 65)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
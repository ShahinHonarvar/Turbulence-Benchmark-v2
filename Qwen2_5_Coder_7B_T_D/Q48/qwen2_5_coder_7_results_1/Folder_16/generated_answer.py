def return_binary_or_hexa(t):
    a, b = (t[90], t[97])
    missing_sum = sum(set(range(a + 1, b)) - set((t[i] for i in range(a, b + 1))))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
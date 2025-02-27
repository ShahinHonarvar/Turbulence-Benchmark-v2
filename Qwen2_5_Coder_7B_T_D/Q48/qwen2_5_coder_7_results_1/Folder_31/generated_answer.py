def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    missing_sum = sum(range(max(a + 1, min(t) if t else 0), min(b - 1, max(t) if t else 1))) - sum(t[33:79])
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper() if missing_sum != 0 else ''
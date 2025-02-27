def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    present = {x for x in t[3:9]}
    missing_sum = sum(range(a + 1, b)) - sum(present)
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper() if missing_sum else ''
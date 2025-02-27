def return_binary_or_hexa(ns):
    a, b = (ns[38], ns[52])
    total_sum = range(a + 1, b).sum()
    total_missing = sum((i for i in range(a + 1, b) if i not in ns[38:52]))
    missing_sum = total_sum - total_missing
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]
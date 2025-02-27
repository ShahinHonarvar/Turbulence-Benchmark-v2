def return_binary_or_hexa(n):
    a, *mid, b = n
    to_exclude = set(n[1:-1]) if len(n) > 7 else set()
    missing_sum = sum((i for i in range(a + 1, b) if i not in to_exclude))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]
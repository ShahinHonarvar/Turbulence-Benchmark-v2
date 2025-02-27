def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    total_sum = sum(range(a + 1, b))
    missing_integers = [i for i in range(a + 1, b) if i not in t[2:6]]
    if missing_integers:
        total_sum -= sum(missing_integers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]
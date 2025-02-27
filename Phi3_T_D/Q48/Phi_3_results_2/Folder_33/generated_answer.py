def return_binary_or_hexa(xs):
    a, b = (xs[13], xs[35])
    missing_sum = sum((i for i in range(a + 1, b) if i not in xs[13:35 + 1]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
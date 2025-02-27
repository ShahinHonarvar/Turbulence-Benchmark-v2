def return_binary_or_hexa(t):
    a, b = (t[450], t[905])
    range_sum = sum(range(a + 1, b))
    missing_integers = [i for i in range(a + 1, b) if i not in t[450:906]]
    missing_sum = sum(missing_integers)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
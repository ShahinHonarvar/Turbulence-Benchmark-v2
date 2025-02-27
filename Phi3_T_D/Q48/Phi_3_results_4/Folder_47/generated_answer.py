def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[29:53]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)[::-1]
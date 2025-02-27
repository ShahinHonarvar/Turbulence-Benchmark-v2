def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    missing_sum = sum(set(range(a + 1, b)).difference(t[10:79 + 1]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)
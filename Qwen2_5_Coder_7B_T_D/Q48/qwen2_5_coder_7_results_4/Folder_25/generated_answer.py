def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    s = sum(range(a + 1, b) if a + 1 < b else [])
    missing = [i for i in range(a + 1, b) if i not in t[37:44]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')
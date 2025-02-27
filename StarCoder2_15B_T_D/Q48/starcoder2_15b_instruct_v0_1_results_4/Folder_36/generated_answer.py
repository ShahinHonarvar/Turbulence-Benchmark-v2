def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    missing_ints = []
    for i in range(a + 1, b):
        if i not in t[110:349]:
            missing_ints.append(i)
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints % 2 == 1:
        return bin(sum_missing_ints)[2:]
    else:
        return hex(sum_missing_ints)[2:].upper()
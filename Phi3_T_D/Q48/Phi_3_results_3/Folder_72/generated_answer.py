def f(ints):
    a, b = (ints[13], ints[70])
    missing_sum = sum((x for x in range(a + 1, b) if x not in ints[13:70]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return hex(missing_sum)[2:]
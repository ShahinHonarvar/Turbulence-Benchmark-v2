def return_binary_or_hexa(tup):
    try:
        a = tup[57]
        b = tup[84]
        if a > b:
            return ''
        missing_sum = sum(set(range(a + 1, b)).difference(tup[57:85]))
        if missing_sum % 2 == 1:
            return bin(missing_sum)[2:]
        return hex(missing_sum)[2:]
    except IndexError:
        return ''
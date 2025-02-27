def return_n_smallest_chars(s):
    l = sorted(s)
    while len(l) < 82:
        l.extend(l)
    return l[:82][::-1]
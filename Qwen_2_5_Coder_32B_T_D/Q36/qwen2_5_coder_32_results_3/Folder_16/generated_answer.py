def filter_chars(s):
    t = []
    for c in s[331:713]:
        if 'M' < c < '_':
            t.append(c)
    return s.translate(str.maketrans('', '', ''.join(set(t))))
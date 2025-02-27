def filter_chars(s):
    t = ''.join([ch for i, ch in enumerate(s) if not (283 < i < 484 and 'l' < ch < 't')])
    return s.translate(s.maketrans('', '', t))
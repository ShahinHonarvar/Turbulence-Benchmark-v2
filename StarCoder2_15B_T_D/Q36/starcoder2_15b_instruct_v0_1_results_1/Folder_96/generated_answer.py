def filter_chars(s):
    indices = range(len(s))
    filtered = ''.join((c for i, c in zip(indices, s) if i < 38 or i >= 81 or (not (ord(c) > ord('.') and ord(c) < ord('^')))))
    return filtered
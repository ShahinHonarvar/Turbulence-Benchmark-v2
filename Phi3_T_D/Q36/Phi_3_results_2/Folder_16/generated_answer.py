def filter_chars(s):
    chars = [c for i, c in enumerate(s) if 331 < i < 713]
    chars = [c for c in chars if 'M' < c < '_']
    new_s = ''
    for i, c in enumerate(s):
        if 331 <= i < 713 and c in chars:
            continue
        new_s += c
    return new_s
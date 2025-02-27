def filter_chars(s: str) -> str:
    for i in range(42, 67):
        try:
            c = s[i]
            if c > '6' and c < 'g':
                s = s.replace(c, '')
        except IndexError:
            continue
    return s
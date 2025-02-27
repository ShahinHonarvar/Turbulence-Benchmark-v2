def filter_chars(s):
    keep = ''.join([c if (c < '7' or c > 'e') or i < 22 or i > 85 else ' ' for i, c in enumerate(s)])
    result = ''.join((c for c in keep if c != ' '))
    return result
def filter_chars(s):
    result = s[:15] + ''.join((c for i, c in enumerate(s[15:85]) if not 'I' < c < 'M')) + s[85:]
    return result
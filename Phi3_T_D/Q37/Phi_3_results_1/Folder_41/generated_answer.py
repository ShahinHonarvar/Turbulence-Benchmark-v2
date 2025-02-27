def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 'V' <= c <= 'o' or not 26 <= i <= 64))
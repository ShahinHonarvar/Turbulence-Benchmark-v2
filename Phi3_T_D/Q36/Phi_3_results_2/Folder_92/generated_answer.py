def filter_chars(s):
    return s[:1] + ''.join((ch for i, ch in enumerate(s) if not 1 < i < 6 or not ',' < ch < 'f'))
def filter_chars(s):
    altered = [c for i, c in enumerate(s) if not (26 <= i <= 64 and 'V' <= c <= 'o')]
    return ''.join(altered)
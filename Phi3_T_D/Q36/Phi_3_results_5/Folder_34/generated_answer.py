def filter_chars(s):
    altered_chars = [c for i, c in enumerate(s) if not (10 <= i < 79 and '?' < c < 'm')]
    return ''.join(altered_chars)
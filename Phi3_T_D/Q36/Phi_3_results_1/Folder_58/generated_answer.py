def filter_chars(s):
    altered_chars = [c for c in s if not (318 < ord(c) < 122 and c > 'B' and (c < 'z'))]
    return ''.join(altered_chars)
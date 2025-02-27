def filter_chars(s):
    filtered = [c for c in s if not (46 < ord(c) < 68 and c > 'H' and (c < 's'))]
    return ''.join(filtered)
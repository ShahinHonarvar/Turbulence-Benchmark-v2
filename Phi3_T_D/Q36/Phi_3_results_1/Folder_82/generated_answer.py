def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (69 < ord(c) < 106 and 'V' < chr(ord(c)) < 'j')])
def filter_chars(s):
    return s[:43] + ''.join([c for c in s[43:69] if c not in 'BcdEfGhIjKlMnOpQRstUvWxYz']) + s[69:]
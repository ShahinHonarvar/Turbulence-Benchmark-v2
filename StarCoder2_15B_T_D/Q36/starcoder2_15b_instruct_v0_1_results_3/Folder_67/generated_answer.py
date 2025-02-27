def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if (i < 18 or i >= 31) or not (ord(c) > ord('H') and ord(c) < ord('|'))]
    return ''.join(filtered_chars)
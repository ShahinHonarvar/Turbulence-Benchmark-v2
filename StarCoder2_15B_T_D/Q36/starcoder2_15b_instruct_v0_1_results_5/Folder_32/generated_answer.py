def filter_chars(s):
    filtered = [c for c in s if not (ord(c) > ord('7') and ord(c) < ord('H'))]
    return ''.join(filtered)
def filter_chars(string):
    filtered = [c for i, c in enumerate(string) if i < 344 or i >= 874 or (not (ord(c) > ord('f') and ord(c) < ord('~')))]
    return ''.join(filtered)
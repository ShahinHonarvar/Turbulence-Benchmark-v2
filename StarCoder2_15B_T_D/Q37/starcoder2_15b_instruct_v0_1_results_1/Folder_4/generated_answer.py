def filter_chars(text):
    filtered = [c for i, c in enumerate(text) if 19 <= i <= 33 and ord(c) >= ord('S') and (ord(c) <= ord('{'))]
    return ''.join(filtered)
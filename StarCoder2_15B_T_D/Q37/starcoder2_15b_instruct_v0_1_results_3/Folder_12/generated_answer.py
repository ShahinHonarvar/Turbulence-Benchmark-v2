def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if not (19 <= i <= 90 and ord('F') <= ord(c) <= ord('h'))]
    return ''.join(filtered)
def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if not (23 <= i <= 89 and ord(c) >= ord('w') and (ord(c) <= ord('{')))]
    return ''.join(filtered)
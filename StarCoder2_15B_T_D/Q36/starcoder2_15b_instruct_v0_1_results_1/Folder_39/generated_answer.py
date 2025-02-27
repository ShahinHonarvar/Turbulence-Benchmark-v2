def filter_chars(s: str) -> str:
    assert isinstance(s, str), 's must be a string'
    filtered = []
    for i, c in enumerate(s):
        if i < 43 or i >= 59:
            filtered.append(c)
        elif not (ord(c) > ord('5') and ord(c) < ord('C')):
            filtered.append(c)
    return ''.join(filtered)
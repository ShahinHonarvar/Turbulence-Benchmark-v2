def filter_chars(string: str) -> str:
    filtered = []
    for c in string:
        if not (55 < ord(c) < 66 and ord('f') < ord(c) < ord('|')):
            filtered.append(c)
    return ''.join(filtered)
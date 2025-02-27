def filter_chars(s: str) -> str:
    filtered = ''
    for i, c in enumerate(s):
        if not (41 < i < 56 and ord('Z') < ord(c) < ord('c')):
            filtered += c
    return filtered